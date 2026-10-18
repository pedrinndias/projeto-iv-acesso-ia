"""
Etapa 3 do piloto do desfecho: snapshots do Wayback das paginas de disponibilidade
regional do Amazon Bedrock. Ver docs/piloto/PROMPT-piloto-desfecho.md.

Paginas:
    models-regions.html               pagina antiga; esvaziada em 2026 ("has moved")
    models-region-compatibility.html  pagina nova, arquivada desde 2026-03-11

Economia: a API CDX devolve o digest (hash do conteudo) de cada snapshot. Snapshots
com o mesmo digest tem conteudo identico, entao so um por digest e baixado; cada dia
herda o resultado do seu digest.

Uso:
    python3 src/coleta/piloto_wayback_bedrock.py listar
    python3 src/coleta/piloto_wayback_bedrock.py baixar
    python3 src/coleta/piloto_wayback_bedrock.py parsear

Saidas:
    dados/intermediario/piloto_cdx.csv            dia, pagina, timestamp, digest
    dados/bruto/wayback_<pagina>_<timestamp>.html um arquivo por digest (sem subpasta:
                                                  o .gitignore so cobre dados/bruto/*.html)
    dados/intermediario/piloto_presenca.csv       (subcomando parsear)
    linhas em dados/intermediario/piloto_fontes.csv
"""
import csv
import hashlib
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
BRUTO = RAIZ / "dados" / "bruto"
INTER = RAIZ / "dados" / "intermediario"
UA = {"User-Agent": "projeto-iv-pucminas/1.0"}
CDX = "https://web.archive.org/cdx/search/cdx"
PAGINAS = {
    "models-regions": "docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html",
    "models-region-compatibility": "docs.aws.amazon.com/bedrock/latest/userguide/models-region-compatibility.html",
}
# Um pouco antes do primeiro modelo do piloto (2024-06-20), para ter o limite inferior,
# ate o fim da janela de observacao do estudo.
INICIO, FIM = "20240501", "20260630"


def pedir(url, timeout=120, tentativas=5):
    """GET com espera progressiva para 429/5xx e para a pagina HTML de limitacao."""
    espera = 10
    for n in range(1, tentativas + 1):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code not in (429, 500, 502, 503, 504) or n == tentativas:
                raise
        except (urllib.error.URLError, TimeoutError):
            if n == tentativas:
                raise
        print(f"    falha temporaria, tentativa {n}/{tentativas}; aguardando {espera}s", flush=True)
        time.sleep(espera)
        espera *= 2


def listar():
    linhas = []
    for nome, url in PAGINAS.items():
        q = urllib.parse.urlencode({"url": url, "output": "json",
                                    "fl": "timestamp,digest", "collapse": "timestamp:8",
                                    "filter": "statuscode:200", "limit": 5000})
        for _ in range(4):
            corpo = pedir(f"{CDX}?{q}").decode("utf-8", "replace").strip()
            if corpo.startswith("["):
                break
            time.sleep(15)  # pagina de limitacao em HTML com status 200
        else:
            raise RuntimeError(f"CDX indisponivel: {nome}")
        dias = [(ts, dg) for ts, dg in json.loads(corpo)[1:] if INICIO <= ts[:8] <= FIM]
        linhas += [(ts[:8], nome, ts, dg) for ts, dg in dias]
        print(f"{nome}: {len(dias)} dias na janela | {len({d for _, d in dias})} digests distintos"
              f" | {dias[0][0][:8] if dias else '-'} a {dias[-1][0][:8] if dias else '-'}")
        time.sleep(3)
    with open(INTER / "piloto_cdx.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["dia", "pagina", "timestamp", "digest"])
        w.writerows(sorted(linhas))
    print("saida -> dados/intermediario/piloto_cdx.csv")


def a_baixar():
    """Um timestamp por (pagina, digest): o primeiro em que o conteudo apareceu."""
    escolhidos = {}
    with open(INTER / "piloto_cdx.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            escolhidos.setdefault((r["pagina"], r["digest"]), r["timestamp"])
    return sorted((p, ts, dg) for (p, dg), ts in escolhidos.items())


def arquivo(pagina, ts):
    return BRUTO / f"wayback_{pagina}_{ts}.html"


def baixar(amostra=None):
    alvos = a_baixar()
    if amostra:
        alvos = [a for a in alvos if a[1] in amostra]
    feitos, falhas = 0, []
    with open(INTER / "piloto_fontes.csv", "a", newline="", encoding="utf-8") as fontes:
        w = csv.writer(fontes)
        for pagina, ts, dg in alvos:
            destino = arquivo(pagina, ts)
            if destino.exists():
                continue  # retomavel: o que ja foi baixado nao e baixado de novo
            url = f"https://web.archive.org/web/{ts}id_/https://{PAGINAS[pagina]}"
            try:
                conteudo = pedir(url)
            except Exception as e:  # um snapshot defeituoso nao derruba os demais
                falhas.append((pagina, ts, str(e)[:60]))
                print(f"  FALHOU {pagina} {ts}: {str(e)[:60]}", flush=True)
                continue
            destino.write_bytes(conteudo)
            w.writerow([url, ts, str(destino.relative_to(RAIZ)), hashlib.sha256(conteudo).hexdigest(),
                        datetime.now(timezone.utc).isoformat(timespec="seconds"),
                        "src/coleta/piloto_wayback_bedrock.py"])
            fontes.flush()
            feitos += 1
            if feitos % 20 == 0:
                print(f"  {feitos} baixados (ultimo {pagina} {ts})", flush=True)
            time.sleep(4)
    print(f"baixados agora: {feitos} | falhas: {len(falhas)} | alvos no total: {len(alvos)}")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "listar":
        listar()
    elif cmd == "baixar":
        baixar(set(sys.argv[2:]) or None)
    elif cmd == "parsear":
        from piloto_parser_bedrock import parsear
        parsear()
    else:
        print(__doc__)
