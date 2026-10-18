"""
Parser dos snapshots do Wayback baixados por piloto_wayback_bedrock.py.

Tres layouts conhecidos (aprendidos em 3 amostras em 03/10/2026):

  A. models-regions.html, 2024: uma tabela; linha = modelo ("Anthropic Claude 3.5
     Sonnet"), coluna = regiao por nome de exibicao ("Asia Pacific (Mumbai)"), celula
     Yes / No / Gated / "Yes (48K context window only)". A tabela traz so as regioes
     "fora das principais"; regiao sem coluna = nao observada (nenhuma linha gravada).
  B. models-regions.html, 2025: colunas Provider, Model e regioes; celula Yes / Yes* / No.
     Uma segunda tabela traz os modelos com data de descontinuacao.
  Nos layouts A e B o tipo gravado e "qualquer" (acessivel de alguma forma) e, para
  "Yes*", tambem "so_cross_region". Nao ha In-Region na pagina antiga: ver comentario
  em parse_antigo.
  C. models-region-compatibility.html, 2026: uma tabela por modelo, com o nome na
     <caption>; linha = regiao (codigo em <code>), colunas In-Region / Geo / Global;
     celula = icone icon-yes / icon-no ou texto ("Legacy (EOL: 2026-05-31)").

Situacao gravada:
    presente   celula afirma disponibilidade (Yes, Yes*, Gated, icone yes, Legacy...)
    ausente    celula nega (No, icone no)
    modelo_ausente   pagina informativa, mas sem o modelo (antes do lancamento ou
                     depois da retirada; a etapa 4 decide qual)
    sem_info   pagina sem tabela de regioes (aviso "has moved", layout desconhecido)
O valor bruto da celula vai junto, para a etapa 4 decidir o que conta como disponivel
(por exemplo, se Gated e Legacy valem).
"""
import csv
import gzip
import re
import html as h
from pathlib import Path

from piloto_eventos_datados import regioes_em

RAIZ = Path(__file__).resolve().parents[2]
BRUTO = RAIZ / "dados" / "bruto"
INTER = RAIZ / "dados" / "intermediario"

PILOTO = {
    "claude 3.5 sonnet": "Claude 3.5 Sonnet",
    "claude 3.5 sonnet v1": "Claude 3.5 Sonnet",
    "claude 3.5 sonnet v2": "Claude 3.5 Sonnet v2",
    "claude 3.7 sonnet": "Claude 3.7 Sonnet",
    "claude sonnet 4.5": "Claude Sonnet 4.5",
    "claude sonnet 4.6": "Claude Sonnet 4.6",
}


def ler(arq):
    b = arq.read_bytes()
    while b[:2] == b"\x1f\x8b":  # o Wayback devolve o corpo original, comprimido
        b = gzip.decompress(b)
    return b.decode("utf-8", "replace")


def txt(s):
    return h.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s))).strip()


def modelo_piloto(nome):
    n = txt(nome).lower().replace("anthropic", " ")
    n = re.sub(r"\(.*?\)", " ", n)          # "(200K context window)"
    n = re.sub(r":\d+\b", " ", n)            # "V2:0"
    n = re.sub(r"[^a-z0-9.]+", " ", n).strip()
    return PILOTO.get(n)


def celulas(tr):
    return re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", tr, re.S)


def valor(c):
    if "icon-yes" in c:
        return "icon-yes"
    if "icon-no" in c:
        return "icon-no"
    return txt(c)


def situacao(v):
    b = v.lower()
    if b in ("no", "icon-no", "", "-", "n/a"):
        return "ausente"
    return "presente"


def regiao_de(cab):
    cods = regioes_em(txt(cab))
    return cods[0] if len(cods) == 1 else ""


def parse_antigo(t):
    """Layouts A e B. Devolve linhas (modelo, regiao, tipo, situacao, valor)."""
    linhas, informativa = [], False
    for tb in re.findall(r"<table.*?</table>", t, re.S):
        trs = re.findall(r"<tr.*?</tr>", tb, re.S)
        if not trs:
            continue
        cab = celulas(trs[0])
        regs = [regiao_de(c) for c in cab]
        if sum(bool(r) for r in regs) < 2:
            continue  # nao e tabela de regioes
        informativa = True
        col_modelo = 1 if txt(cab[0]).lower() == "provider" else 0
        for tr in trs[1:]:
            cs = celulas(tr)
            if len(cs) != len(cab):
                continue
            m = modelo_piloto(cs[col_modelo])
            if not m:
                continue
            for c, r in zip(cs, regs):
                if not r:
                    continue
                v = valor(c)
                # Nota da pagina (2025): "* Some models are accessible in some Regions only
                # through cross-Region inference". MAS "Yes" sem asterisco NAO quer dizer
                # In-Region: na sobreposicao com a pagina nova (2026-03-12 a 2026-04-20),
                # 94% dos "Yes" da antiga sao Geo/Global na nova. Por isso a pagina antiga
                # so mede "qualquer" (acessivel de alguma forma); o asterisco vira um tipo
                # a parte, "so_cross_region".
                linhas.append((m, r, "qualquer", situacao(v.rstrip("*")), v))
                if v.endswith("*"):
                    linhas.append((m, r, "so_cross_region", "presente", v))
    return linhas, informativa


def parse_novo(t):
    """Layout C."""
    linhas, informativa = [], False
    for tb in re.findall(r"<table.*?</table>", t, re.S):
        cap = re.search(r"<caption>(.*?)</caption>", tb, re.S)
        trs = re.findall(r"<tr.*?</tr>", tb, re.S)
        if not cap or not trs:
            continue
        cab = [txt(c) for c in celulas(trs[0])]
        if cab[:1] != ["Region"]:
            continue
        informativa = True
        m = modelo_piloto(cap.group(1))
        if not m:
            continue
        tipos = [c.lower().replace("-", "_") for c in cab[1:]]   # in_region, geo, global
        for tr in trs[1:]:
            cs = celulas(tr)
            cod = re.search(r"<code[^>]*>([a-z0-9\-]+)</code>", cs[0]) if cs else None
            if not cod or len(cs) != len(cab):
                continue
            for tipo, c in zip(tipos, cs[1:]):
                v = valor(c)
                linhas.append((m, cod.group(1), tipo, situacao(v), v))
    return linhas, informativa


def parsear():
    cdx = list(csv.DictReader(open(INTER / "piloto_cdx.csv", encoding="utf-8")))
    primeiro = {}
    for r in cdx:
        primeiro.setdefault((r["pagina"], r["digest"]), r["timestamp"])
    saida, resumo = [], {}
    for (pagina, digest), ts in sorted(primeiro.items(), key=lambda kv: kv[1]):
        arq = BRUTO / f"wayback_{pagina}_{ts}.html"
        if not arq.exists():
            continue
        t = ler(arq)
        linhas, informativa = (parse_novo if pagina == "models-region-compatibility" else parse_antigo)(t)
        if not informativa:
            saida.append((pagina, ts, digest, "*", "*", "*", "sem_info", "has moved" if "has moved" in t else "sem tabela de regioes"))
            resumo[ts] = "sem_info"
            continue
        achados = {l[0] for l in linhas}
        for m in sorted(set(PILOTO.values()) - achados):
            saida.append((pagina, ts, digest, m, "*", "*", "modelo_ausente", ""))
        saida += [(pagina, ts, digest) + l for l in linhas]
        resumo[ts] = f"{len(achados)} modelos do piloto"
    with open(INTER / "piloto_presenca.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["pagina", "timestamp_conteudo", "digest", "modelo", "regiao", "tipo", "situacao", "valor_bruto"])
        w.writerows(saida)
    return saida, resumo
