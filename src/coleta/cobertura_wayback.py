"""
Mede a cobertura historica das fontes na API CDX do Internet Archive.

Conta dias distintos com registro arquivado, por trimestre. E este levantamento que
define a janela de observacao do estudo. Ver secao 3.1 da Ficha Inicial.

Duas armadilhas da API, tratadas aqui:
  1. Exige HTTPS. Em http:// sem seguir redirecionamento o corpo volta vazio.
  2. Sob limitacao de taxa devolve uma pagina HTML "Temporarily Offline" com status 200,
     em vez de erro. Por isso a resposta e checada antes de ser interpretada como JSON.

Saida:
    dados/intermediario/cobertura_wayback_AAAA-MM-DD.csv
"""
import csv
import json
import time
import urllib.parse
import urllib.request
from collections import Counter
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
INTER = RAIZ / "dados" / "intermediario"
FONTES = Path(__file__).resolve().parent / "fontes.csv"

CDX = "https://web.archive.org/cdx/search/cdx"
TENTATIVAS = 4
ESPERA_INICIAL = 8


def consultar(url, limite=5000):
    params = urllib.parse.urlencode(
        {"url": url, "output": "json", "fl": "timestamp",
         "collapse": "timestamp:8", "limit": limite}
    )
    req = urllib.request.Request(
        f"{CDX}?{params}", headers={"User-Agent": "projeto-iv-pucminas/1.0"}
    )
    espera = ESPERA_INICIAL
    for tentativa in range(1, TENTATIVAS + 1):
        with urllib.request.urlopen(req, timeout=110) as r:
            corpo = r.read().decode("utf-8", "replace").strip()
        if corpo.startswith("["):
            linhas = json.loads(corpo)
            return sorted(x[0] for x in linhas[1:]) if len(linhas) > 1 else []
        if not corpo:
            return []
        print(f"    limitacao de taxa, tentativa {tentativa}/{TENTATIVAS}; "
              f"aguardando {espera}s")
        time.sleep(espera)
        espera *= 2
    raise RuntimeError(f"CDX indisponivel apos {TENTATIVAS} tentativas: {url}")


def trimestre(ts):
    return f"{ts[:4]}Q{(int(ts[4:6]) - 1) // 3 + 1}"


def main():
    INTER.mkdir(parents=True, exist_ok=True)
    hoje = date.today().isoformat()
    saida = INTER / f"cobertura_wayback_{hoje}.csv"

    with open(FONTES, encoding="utf-8") as f:
        fontes = list(csv.DictReader(f))

    registros = []
    for fonte in fontes:
        print(f"  {fonte['apelido']}")
        ts = consultar(fonte["url"])
        if not ts:
            print("    nenhum registro arquivado")
            continue
        por_trimestre = Counter(trimestre(t) for t in ts)
        for tri, n in sorted(por_trimestre.items()):
            registros.append(
                {"apelido": fonte["apelido"], "url": fonte["url"],
                 "bloco": fonte["bloco"], "trimestre": tri, "n_dias": n,
                 "primeiro_registro": ts[0][:8], "ultimo_registro": ts[-1][:8],
                 "total_dias": len(ts), "data_consulta": hoje}
            )
        print(f"    {len(ts)} dias | {ts[0][:8]} a {ts[-1][:8]}")
        time.sleep(3)

    with open(saida, "w", newline="", encoding="utf-8") as f:
        campos = ["apelido", "url", "bloco", "trimestre", "n_dias",
                  "primeiro_registro", "ultimo_registro", "total_dias", "data_consulta"]
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        w.writerows(registros)

    print(f"\nsaida -> {saida.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
