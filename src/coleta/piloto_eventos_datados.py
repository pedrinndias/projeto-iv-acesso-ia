"""
Etapa 2 do piloto do desfecho: eventos DATADOS de disponibilidade dos 5 modelos
Claude do piloto no Amazon Bedrock. Ver docs/piloto/PROMPT-piloto-desfecho.md.

Tres fontes oficiais da AWS:
  1. What's New, pela API publica de diretorio (aws.amazon.com/api/dirs/items/search),
     filtrada pela tag do Amazon Bedrock. Ha dois diretorios: "whats-new" (posts ate
     meados de 2024) e "whats-new-v2" (posts posteriores). Os dois sao consultados.
  2. Historico da documentacao do Bedrock (doc-history.html), ja baixado na etapa 1.
     ATENCAO: tem datas erradas comprovadas (ver docs/piloto/ESTADO.md). Toda data dele
     precisa de segunda fonte.
  3. Blog da AWS, pela mesma API de diretorio (item.directoryId=blog-posts), com busca
     textual. E onde estao os anuncios de expansao regional dos modelos recentes
     (Japao, Canada, Oriente Medio, Sudeste Asiatico, India...). Quando o post nomeia
     so o pais, a coluna regioes recebe "pais:<nome>", e nao um codigo adivinhado.

O tipo de disponibilidade so e atribuido quando o texto o diz explicitamente; no resto
fica "indistinto". A etapa 3 resolve o tipo pelos snapshots.

Saidas:
    dados/bruto/aws_whatsnew_bedrock_<diretorio>_AAAA-MM-DD.json   resposta original
    dados/intermediario/piloto_eventos_datados.csv
    linhas acrescentadas em dados/intermediario/piloto_fontes.csv
"""
import csv
import hashlib
import html
import json
import re
import time
import urllib.parse
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
BRUTO = RAIZ / "dados" / "bruto"
INTER = RAIZ / "dados" / "intermediario"
UA = {"User-Agent": "projeto-iv-pucminas/1.0"}
API = "https://aws.amazon.com/api/dirs/items/search"
INICIO = "2024-01-01"

# Ordem importa: as formas mais especificas vem antes.
MODELOS = [
    ("Claude Sonnet 4.6", r"(?:Claude )?Sonnet 4\.6|sonnet-4-6"),
    ("Claude Sonnet 4.5", r"(?:Claude )?Sonnet 4\.5|sonnet-4-5"),
    ("Claude 3.7 Sonnet", r"Claude 3\.7 Sonnet|3-7-sonnet"),
    ("Claude 3.5 Sonnet v2", r"Claude 3\.5 Sonnet v2|upgraded Claude 3\.5 Sonnet|3-5-sonnet-20241022"),
    ("Claude 3.5 Sonnet", r"Claude 3\.5 Sonnet|3-5-sonnet-20240620"),
]
V2_LANCAMENTO = "2024-10-22"
# Qualquer modelo Claude nomeado, inclusive os que nao estao no piloto.
QUALQUER_CLAUDE = re.compile(
    r"Claude\s+(?:\d(?:\.\d)?\s+)?(?:Opus|Sonnet|Haiku|Fable|Mythos|Instant)(?:\s+\d(?:\.\d)?)?"
    r"|Claude\s+\d(?:\.\d)?", re.I)
DISPONIBILIDADE = re.compile(
    r"now available|available in|available on|is now in Amazon Bedrock|now in Amazon Bedrock"
    r"|more regions|additional regions|region expansion|expands", re.I)
RECURSO = re.compile(
    r"Knowledge Bases|Agents|AgentCore|prompt caching|fine-tun|Distillation|Reserved|Flows"
    r"|Guardrails|console|latency-optimized|evaluation|FedRAMP|batch|Provisioned|legacy", re.I)

# Nome de exibicao da AWS -> codigo. Casado pelo trecho entre parenteses.
REGIOES = {
    "N. Virginia": "us-east-1", "Ohio": "us-east-2", "N. California": "us-west-1",
    "Oregon": "us-west-2", "US-West": "us-gov-west-1", "US-East": "us-gov-east-1",
    "Central)": "ca-central-1", "Calgary": "ca-west-1", "São Paulo": "sa-east-1",
    "Sao Paulo": "sa-east-1", "Frankfurt": "eu-central-1", "Zurich": "eu-central-2",
    "Ireland": "eu-west-1", "London": "eu-west-2", "Paris": "eu-west-3",
    "Stockholm": "eu-north-1", "Milan": "eu-south-1", "Spain": "eu-south-2",
    "Tokyo": "ap-northeast-1", "Seoul": "ap-northeast-2", "Osaka": "ap-northeast-3",
    "Mumbai": "ap-south-1", "Hyderabad": "ap-south-2", "Singapore": "ap-southeast-1",
    "Sydney": "ap-southeast-2", "Jakarta": "ap-southeast-3", "Melbourne": "ap-southeast-4",
    "Malaysia": "ap-southeast-5", "New Zealand": "ap-southeast-6", "Auckland": "ap-southeast-6",
    "Thailand": "ap-southeast-7", "Hong Kong": "ap-east-1", "Taipei": "ap-east-2",
    "Bahrain": "me-south-1", "UAE": "me-central-1", "Tel Aviv": "il-central-1",
    "Cape Town": "af-south-1", "Mexico": "mx-central-1",
}
PAISES = ["Japan", "Australia", "Canada", "South Africa", "India", "New Zealand",
          "Middle East", "UAE", "Bahrain", "Thailand", "Malaysia", "Singapore", "Indonesia",
          "Taiwan", "Korea", "Brazil", "South America", "Europe", "Mexico", "Israel",
          "Switzerland", "Spain", "Germany", "United Kingdom", "Ireland", "France", "Sweden",
          "Italy", "Hong Kong"]
BUSCAS_BLOG = ['"cross-Region inference" Claude', 'Claude "Amazon Bedrock" region availability']
CODIGO = re.compile(r"\b(?:us|ca|sa|eu|ap|me|il|af|mx|eusc)-(?:gov-)?[a-z]+-\d\b")


def texto(s):
    s = re.sub(r"<script.*?</script>", " ", s or "", flags=re.S)
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s))).strip()


def regioes_em(t):
    achadas = set(CODIGO.findall(t))
    for chave, cod in REGIOES.items():
        padrao = re.escape(chave) if chave.endswith(")") else r"\(" + re.escape(chave) + r"\)"
        if chave == "Central)":
            padrao = r"Canada \(Central\)"
        if chave == "Mexico":
            padrao = r"Mexico \(Central\)"
        if re.search(padrao, t):
            achadas.add(cod)
    return sorted(achadas)


def tipo_em(t):
    b = t.lower().replace("-", " ")
    if "global cross region" in b or "global inference" in b:
        return "global"
    if "cross region" in b or "inference profile" in b:
        return "geo"
    if "batch inference" in b:
        return "batch"
    if "provisioned throughput" in b:
        return "provisionado"
    return "indistinto"


def _modelos_com_posicao(t, dia):
    achados, resto = [], t
    for nome, padrao in MODELOS:
        m = re.search(padrao, resto, flags=re.I)
        if m:
            if nome == "Claude 3.5 Sonnet" and dia >= V2_LANCAMENTO:
                nome = "Claude 3.5 Sonnet (v1 ou v2, ambiguo)"
            achados.append((m.start(), nome))
            resto = re.sub(padrao, lambda x: " " * len(x.group(0)), resto, flags=re.I)
    return sorted(achados)


def modelos_em(titulo, corpo, dia):
    """Modelos do piloto a que o texto se refere.

    O titulo manda: se ele nomeia modelos do piloto, sao eles. Se nomeia so outros
    modelos Claude, o texto nao e do piloto (lista vazia). Se nao nomeia nenhum, vale o
    primeiro modelo citado no corpo, e so se ele for do piloto. Isso evita atribuir ao
    3.5 Sonnet um post do 3.7 que se compara a ele. Devolve None para texto sobre
    "modelos Claude" sem nenhum modelo nomeado.
    """
    no_titulo = _modelos_com_posicao(titulo, dia)
    if no_titulo:
        return [n for _, n in no_titulo]
    if QUALQUER_CLAUDE.search(titulo):
        return []
    no_corpo = _modelos_com_posicao(corpo, dia)
    outro = QUALQUER_CLAUDE.search(corpo)
    if no_corpo and (outro is None or no_corpo[0][0] <= outro.start()):
        return [no_corpo[0][1]]
    return [] if outro else None


def registrar_fonte(url, arq, conteudo):
    caminho = INTER / "piloto_fontes.csv"
    novo = not caminho.exists()
    with open(caminho, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if novo:
            w.writerow(["url", "timestamp", "arquivo", "sha256", "data_coleta", "script"])
        w.writerow([url, "", str(arq.relative_to(RAIZ)), hashlib.sha256(conteudo).hexdigest(),
                    datetime.now(timezone.utc).isoformat(timespec="seconds"),
                    "src/coleta/piloto_eventos_datados.py"])


def whats_new(diretorio):
    """Todos os posts com a tag do Bedrock, do mais novo para o mais antigo, ate INICIO."""
    itens, pagina = [], 0
    while True:
        params = urllib.parse.urlencode({
            "item.directoryId": diretorio, "item.locale": "en_US",
            "sort_by": "item.additionalFields.postDateTime", "sort_order": "desc",
            "size": 100, "page": pagina,
            "tags.id": f"{diretorio}#general-products#amazon-bedrock",
        })
        req = urllib.request.Request(f"{API}?{params}", headers=UA)
        with urllib.request.urlopen(req, timeout=60) as r:
            lote = json.loads(r.read())
        novos = lote.get("items", [])
        itens += novos
        if not novos or novos[-1]["item"]["additionalFields"].get("postDateTime", "") < INICIO:
            break
        pagina += 1
        time.sleep(1.5)
    hoje = date.today().isoformat()
    bruto = json.dumps(itens, ensure_ascii=False).encode("utf-8")
    arq = BRUTO / f"aws_whatsnew_bedrock_{diretorio}_{hoje}.json"
    arq.write_bytes(bruto)
    registrar_fonte(f"{API}?item.directoryId={diretorio}&tags.id={diretorio}#general-products#amazon-bedrock", arq, bruto)
    return itens


def natureza(titulo):
    if RECURSO.search(titulo) or not DISPONIBILIDADE.search(titulo):
        return "recurso"
    return "disponibilidade"


def eventos_whats_new():
    eventos, vistos = [], set()
    for diretorio in ("whats-new", "whats-new-v2"):
        for it in whats_new(diretorio):
            a = it["item"]["additionalFields"]
            dia = a.get("postDateTime", "")[:10]
            titulo = texto(a.get("headline", ""))
            url = a.get("headlineUrl", "")
            if url.startswith("/"):
                url = "https://aws.amazon.com" + url
            chave = url or (dia + titulo)
            if dia < INICIO or chave in vistos:
                continue
            vistos.add(chave)  # o mesmo post aparece nos dois diretorios
            corpo = texto(a.get("postBody", ""))
            completo = titulo + " " + corpo
            if "claude" not in completo.lower():
                continue
            mods = modelos_em(titulo, corpo, dia)
            if mods == []:
                continue
            for m in mods or ["Claude (sem modelo nomeado)"]:
                eventos.append([dia, m, natureza(titulo), ";".join(regioes_em(completo)),
                                tipo_em(completo), url, completo[:200]])
    return eventos, len(vistos)


def eventos_blog():
    eventos, vistos, hoje = [], set(), date.today().isoformat()
    for n, q in enumerate(BUSCAS_BLOG, 1):
        params = urllib.parse.urlencode({
            "item.directoryId": "blog-posts", "item.locale": "en_US",
            "sort_by": "item.additionalFields.createdDate", "sort_order": "desc",
            "size": 100, "q": q, "q_operator": "AND"})
        url_api = f"{API}?{params}"
        with urllib.request.urlopen(urllib.request.Request(url_api, headers=UA), timeout=60) as r:
            bruto = r.read()
        arq = BRUTO / f"aws_blog_busca{n}_{hoje}.json"
        arq.write_bytes(bruto)
        registrar_fonte(url_api, arq, bruto)
        time.sleep(1.5)
        for it in json.loads(bruto).get("items", []):
            a = it["item"]["additionalFields"]
            dia = (a.get("createdDate") or "")[:10]
            link = a.get("link", "")
            if dia < INICIO or link in vistos:
                continue
            vistos.add(link)
            titulo, resumo = texto(a.get("title", "")), texto(a.get("postExcerpt", ""))
            completo = titulo + " " + resumo
            if "claude" not in completo.lower():
                continue
            # No blog os posts de expansao LISTAM os modelos atendidos ("Opus 4.6, Sonnet
            # 4.6 e Haiku 4.5..."). Por isso, sem modelo no titulo, valem todos os modelos
            # do piloto citados no resumo, e nao so o primeiro, como no What's New.
            no_titulo = [n for _, n in _modelos_com_posicao(titulo, dia)]
            if no_titulo:
                mods = no_titulo
            elif QUALQUER_CLAUDE.search(titulo):
                continue
            else:
                mods = [n for _, n in _modelos_com_posicao(resumo, dia)] or None
            regs = regioes_em(completo) + ["pais:" + p for p in PAISES if re.search(r"\b" + p + r"\b", titulo)]
            nat = "disponibilidade" if regs and ("inferenc" in completo.lower() or "availab" in completo.lower()) else "recurso"
            for m in mods or ["Claude (sem modelo nomeado)"]:
                eventos.append([dia, m, nat, ";".join(regs), tipo_em(completo), link, completo[:200]])
    return eventos


def eventos_doc_history() -> list[list[str]]:
    arquivos = sorted(BRUTO.glob("aws_bedrock_doc-history_*.html"))
    if not arquivos:
        raise SystemExit("doc-history bruto nao encontrado; rode a etapa 1")
    t = arquivos[-1].read_text(encoding="utf-8", errors="replace")
    url = "https://docs.aws.amazon.com/bedrock/latest/userguide/doc-history.html"
    eventos: list[list[str]] = []
    for tr in re.findall(r"<tr>(.*?)</tr>", t, flags=re.S):
        cel = [texto(c) for c in re.findall(r"<td[^>]*>(.*?)</td>", tr, flags=re.S)]
        if len(cel) < 3 or "claude" not in " ".join(cel).lower():
            continue
        try:
            dia = datetime.strptime(cel[-1], "%B %d, %Y").date().isoformat()
        except ValueError:
            continue
        corpo = cel[0] + ": " + cel[1]
        # No anúncio de batch, a cláusula do Titan lista regiões de outro modelo.
        trecho_claude = corpo.partition(" and Amazon Titan Text Embeddings V2 in ")[0]
        for m in modelos_em(cel[0], cel[1], dia) or []:
            nat = (
                "disponibilidade"
                if re.match(r"New model|Region expansion$", cel[0])
                else "recurso"
            )
            eventos.append(
                [
                    dia,
                    m,
                    nat,
                    ";".join(regioes_em(trecho_claude)),
                    tipo_em(corpo),
                    url + " (doc-history; datas exigem 2a fonte)",
                    corpo[:200],
                ]
            )
    return eventos


def main():
    wn, n_posts = eventos_whats_new()
    bl = eventos_blog()
    dh = eventos_doc_history()
    todos = sorted(wn + bl + dh, key=lambda e: (e[1], e[0]))
    with open(INTER / "piloto_eventos_datados.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["data", "modelo", "natureza", "regioes", "tipo", "url", "trecho"])
        w.writerows(todos)

    print(f"posts distintos do Bedrock no What's New desde {INICIO}: {n_posts}")
    print(f"eventos: {len(wn)} do What's New + {len(bl)} do blog + {len(dh)} do doc-history = {len(todos)}")
    print("\nso natureza=disponibilidade, por modelo (What's New+blog | doc-history | com regiao ou pais):")
    disp = [e for e in todos if e[2] == "disponibilidade"]
    for m in sorted({e[1] for e in disp}):
        a = sum(e[1] == m and "doc-history" not in e[5] for e in disp)
        b = sum(e[1] == m and "doc-history" in e[5] for e in disp)
        c = sum(e[1] == m and e[3] != "" for e in disp)
        print(f"  {m:42s} {a:3d} | {b:3d} | {c:3d}")
    print("\neventos de disponibilidade com regiao nomeada:")
    for e in disp:
        if e[3]:
            print(f"  {e[0]} {e[1][:26]:26s} {e[4]:10s} {e[3][:60]}")
    print("\nsaida -> dados/intermediario/piloto_eventos_datados.csv")


if __name__ == "__main__":
    main()
