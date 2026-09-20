"""
Mede o historico de commits da documentacao do Microsoft Foundry no GitHub.

Esta e a sexta linha da tabela 3.1 da Ficha Inicial, a unica que os outros dois
scripts de coleta nao reproduzem: ela nao vem da API CDX do Internet Archive, e
sim da API de commits do GitHub. Por isso nao esta em fontes.csv.

ARMADILHA QUE ESTE SCRIPT EXISTE PARA EVITAR:

    A API de commits do GitHub NAO segue renomeacao de arquivo. Consultar um
    unico caminho devolve apenas os commits posteriores a ultima mudanca de
    nome, e o historico anterior fica invisivel.

    O arquivo da documentacao do Foundry foi renomeado ao menos uma vez. Medido
    em 20/09/2026, o caminho antigo tem 125 commits e ja nao existe; o caminho
    sucessor tem outras dezenas. Uma consulta a um caminho so subestima o
    historico em uma ordem de grandeza.

Por isso o script consulta a cadeia inteira de caminhos conhecidos e soma.
Ao descobrir um novo nome do arquivo, acrescente-o a CAMINHOS.

Saida:
    dados/intermediario/historico_repo_microsoft_AAAA-MM-DD.csv
"""
import csv
import json
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
INTER = RAIZ / "dados" / "intermediario"

REPO = "MicrosoftDocs/azure-ai-docs"
CAMINHOS = [
    "articles/ai-foundry/concepts/models-featured.md",
    "articles/ai-foundry/concepts/foundry-models-overview.md",
]
API = "https://api.github.com"
CAB = {"Accept": "application/vnd.github+json",
       "User-Agent": "projeto-iv-pucminas/1.0"}


def _pedir(url):
    req = urllib.request.Request(url, headers=CAB)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read()), dict(r.headers)


def commits(caminho):
    """Todos os commits de um caminho, paginando ate o fim."""
    datas, pagina = [], 1
    while True:
        url = f"{API}/repos/{REPO}/commits?path={caminho}&per_page=100&page={pagina}"
        try:
            lote, _ = _pedir(url)
        except urllib.error.HTTPError as e:
            if e.code == 403:
                raise RuntimeError(
                    "GitHub recusou: limite de 60 consultas por hora sem "
                    "autenticacao. Espere ou defina um token."
                ) from e
            raise
        if not lote:
            break
        datas += [c["commit"]["committer"]["date"][:10] for c in lote]
        if len(lote) < 100:
            break
        pagina += 1
    return sorted(datas)


def existe(caminho):
    try:
        _pedir(f"{API}/repos/{REPO}/contents/{caminho}")
        return True
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return False
        raise


def main():
    INTER.mkdir(parents=True, exist_ok=True)
    hoje = date.today().isoformat()
    linhas, todas = [], []

    for caminho in CAMINHOS:
        datas = commits(caminho)
        vivo = existe(caminho)
        todas += datas
        linhas.append({
            "repositorio": REPO,
            "caminho": caminho,
            "existe_hoje": "sim" if vivo else "nao",
            "n_commits": len(datas),
            "primeiro": datas[0] if datas else "",
            "ultimo": datas[-1] if datas else "",
            "data_consulta": hoje,
        })
        print(f"  {caminho}")
        print(f"    {len(datas):>4} commits | {datas[0] if datas else '-'} a "
              f"{datas[-1] if datas else '-'} | existe hoje: {'sim' if vivo else 'nao'}")

    todas.sort()
    linhas.append({
        "repositorio": REPO,
        "caminho": "TOTAL (cadeia de renomeacoes)",
        "existe_hoje": "-",
        "n_commits": len(todas),
        "primeiro": todas[0] if todas else "",
        "ultimo": todas[-1] if todas else "",
        "data_consulta": hoje,
    })

    saida = INTER / f"historico_repo_microsoft_{hoje}.csv"
    with open(saida, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0]))
        w.writeheader()
        w.writerows(linhas)

    print(f"\n  TOTAL: {len(todas)} commits | {todas[0]} a {todas[-1]}")
    print(f"\nsaida -> {saida.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
