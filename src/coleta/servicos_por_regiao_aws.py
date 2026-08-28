"""
Baixa o indice publico de disponibilidade de servicos da AWS por regiao.

Gera a variavel de controle de maturidade da regiao (n_servicos_total), usada para
distinguir atraso especifico de IA de atraso geral de infraestrutura. Ver secao 3.2
da Ficha Inicial.

Saidas:
    dados/bruto/aws_servicos_regiao_AAAA-MM-DD.json   resposta original
    dados/intermediario/aws_servicos_por_regiao.csv   contagem por regiao
    dados/intermediario/aws_servico_regiao.csv        par servico x regiao
"""
import json
import csv
import urllib.request
from collections import Counter
from datetime import date, datetime, timezone
from pathlib import Path

URL = "https://api.regional-table.region-services.aws.a2z.com/index.json"
RAIZ = Path(__file__).resolve().parents[2]
BRUTO = RAIZ / "dados" / "bruto"
INTER = RAIZ / "dados" / "intermediario"


def baixar():
    req = urllib.request.Request(URL, headers={"User-Agent": "projeto-iv-pucminas/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def main():
    BRUTO.mkdir(parents=True, exist_ok=True)
    INTER.mkdir(parents=True, exist_ok=True)
    hoje = date.today().isoformat()

    dados = baixar()
    pares = dados["prices"]

    caminho_bruto = BRUTO / f"aws_servicos_regiao_{hoje}.json"
    caminho_bruto.write_text(json.dumps(dados, ensure_ascii=False), encoding="utf-8")

    (BRUTO / f"aws_servicos_regiao_{hoje}.meta.json").write_text(
        json.dumps(
            {
                "url": URL,
                "coletado_em": datetime.now(timezone.utc).isoformat(),
                "script": "src/coleta/servicos_por_regiao_aws.py",
                "n_pares": len(pares),
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    linhas = [
        (p["attributes"]["aws:region"], p["attributes"]["aws:serviceName"])
        for p in pares
    ]

    with open(INTER / "aws_servico_regiao.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["regiao", "servico", "data_coleta"])
        for regiao, servico in sorted(linhas):
            w.writerow([regiao, servico, hoje])

    contagem = Counter(r for r, _ in linhas)
    referencia = contagem.get("us-east-1", 0)

    with open(INTER / "aws_servicos_por_regiao.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["regiao", "n_servicos", "prop_vs_us_east_1", "data_coleta"])
        for regiao, n in contagem.most_common():
            prop = round(n / referencia, 4) if referencia else ""
            w.writerow([regiao, n, prop, hoje])

    print(f"pares servico x regiao : {len(linhas)}")
    print(f"regioes                : {len(contagem)}")
    print(f"referencia us-east-1   : {referencia} servicos")
    for regiao in ("sa-east-1", "eu-west-1", "us-west-2"):
        n = contagem.get(regiao, 0)
        pct = f"{n / referencia:.0%}" if referencia else "-"
        print(f"  {regiao:14s} {n:4d}  ({pct} da referencia)")
    print(f"\nbruto  -> {caminho_bruto.relative_to(RAIZ)}")
    print(f"saidas -> dados/intermediario/aws_servico_regiao.csv")
    print(f"          dados/intermediario/aws_servicos_por_regiao.csv")


if __name__ == "__main__":
    main()
