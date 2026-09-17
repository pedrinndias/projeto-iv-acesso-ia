"""
Reproduz as consultas registradas em log-busca.csv.

Executa as expressoes de busca nas tres bases de acesso irrestrito usadas na
calibracao e confere, consulta a consulta, quais artigos do conjunto-controle
sao recuperados. Scopus, ACM DL e IEEE Xplore nao entram aqui: exigem
assinatura institucional e foram deixadas para execucao manual.

Duas armadilhas tratadas:
  1. OpenAlex mantem um "polite pool" que exige o parametro mailto na query
     string, nao apenas no User-Agent. Sem ele a API devolve 429 em rajada.
  2. A SBC OpenLib nao expoe contagem em JSON. O total aparece no HTML no
     formato "1 a 25 de 535 itens"; e esse numero que e extraido.

Uso:
    python3 buscas.py            # roda tudo
    python3 buscas.py openalex   # so uma base
"""
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

MAIL = "pedro3soares@gmail.com"
UA = {"User-Agent": f"projeto-iv-pucminas/1.0 (mailto:{MAIL})"}

CONTROLE = {
    "Lutz (2019)":          "10.1002/hbe2.140",
    "Ahmed & Wahed (2020)": "10.48550/arXiv.2010.15581",
    "Mannuru et al. (2023)": "10.1177/02666669231200628",
    "Wang et al. (2024)":   "10.1177/14614448241232345",
    "Sastry et al. (2024)": "10.48550/arXiv.2402.08797",
}

B1 = ('("artificial intelligence" OR "generative AI" OR "large language model" '
      'OR "foundation model" OR "computing power")')
LINHA_A = ('("digital divide" OR "digital inequality" OR "digital inequalities" '
           'OR "compute divide" OR "AI divide" OR "artificial intelligence divide" '
           'OR "unequal access" OR "access gap")')
LINHA_B = ('("developing countries" OR "global south" OR "digital sovereignty" '
           'OR "AI governance" OR "compute governance" '
           'OR "governance of artificial intelligence")')
FILTROS = ",from_publication_date:2019-01-01,type:article|preprint"


def _ler(url, timeout=90):
    return urllib.request.urlopen(
        urllib.request.Request(url, headers=UA), timeout=timeout
    ).read().decode("utf-8", "replace")


def openalex(filtro):
    """Numero de registros. Reenvia com espera crescente diante de 429."""
    url = ("https://api.openalex.org/works?filter="
           + urllib.parse.quote(filtro, safe=':,()"|')
           + "&per-page=1&mailto=" + MAIL)
    espera = 20
    for _ in range(7):
        try:
            n = json.loads(_ler(url))["meta"]["count"]
            time.sleep(2.5)
            return n
        except urllib.error.HTTPError as e:
            if e.code != 429:
                raise
            time.sleep(espera)
            espera = min(espera * 2, 240)
    raise RuntimeError("OpenAlex indisponivel apos 7 tentativas: " + filtro)


def arxiv(expr):
    url = ("https://export.arxiv.org/api/query?search_query="
           + urllib.parse.quote(expr, safe='') + "&max_results=1")
    m = re.search(r"<opensearch:totalResults[^>]*>(\d+)<", _ler(url))
    time.sleep(3.5)
    return int(m.group(1)) if m else None


def sbc_openlib(termos):
    url = ("https://sol.sbc.org.br/busca/index.php/integrada/results?query="
           + urllib.parse.quote(termos, safe=''))
    texto = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", _ler(url))))
    time.sleep(2.5)
    m = re.findall(r"de (\d[\d.]*) itens", texto)
    return m[-1] if m else "0"


def roda_openalex():
    print("\n=== OpenAlex (titulo e resumo; a partir de 2019; artigo ou preprint) ===")
    for rotulo, bloco in (("LINHA A", LINHA_A), ("LINHA B", LINHA_B)):
        filtro = f"title_and_abstract.search:{B1} AND {bloco}" + FILTROS
        total = openalex(filtro)
        recuperados = [
            nome for nome, doi in CONTROLE.items()
            if openalex(f"doi:https://doi.org/{doi}," + filtro) == 1
        ]
        print(f"\n{rotulo}: {total} resultados | controle {len(recuperados)}/5")
        for nome in CONTROLE:
            print(f"   {'OK ' if nome in recuperados else '-- '} {nome}")


def roda_arxiv():
    print("\n=== arXiv (campo abs) ===")
    expr = ('(abs:"artificial intelligence" OR abs:"generative AI" '
            'OR abs:"computing power") AND (abs:"digital divide" '
            'OR abs:"compute divide" OR abs:"unequal access" '
            'OR abs:"digital sovereignty" OR abs:"developing countries")')
    print(f"   expressao final : {arxiv(expr)} resultados")
    v1 = 'abs:"generative AI" AND abs:"adoption lag" AND abs:"data residency"'
    print(f"   v1 estreita     : {arxiv(v1)} resultados")


def roda_sbc():
    print("\n=== SBC OpenLib (busca integrada) ===")
    for termos in ("soberania digital inteligência artificial",
                   "desigualdade digital inteligência artificial",
                   "computação em nuvem disponibilidade região",
                   "difusão tecnológica inteligência artificial"):
        print(f"   {sbc_openlib(termos):>6}  {termos}")


def main():
    alvos = {"openalex": roda_openalex, "arxiv": roda_arxiv, "sbc": roda_sbc}
    pedidos = sys.argv[1:] or list(alvos)
    for nome in pedidos:
        if nome not in alvos:
            print(f"base desconhecida: {nome}; use {', '.join(alvos)}")
            return 1
        alvos[nome]()
    return 0


if __name__ == "__main__":
    sys.exit(main())
