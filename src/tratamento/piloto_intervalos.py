"""
Etapa 4 do piloto do desfecho: intervalos de chegada de cada modelo a cada regiao e
precisao com que essa data pode ser determinada. Ver docs/piloto/PROMPT-piloto-desfecho.md.

Definicao (decisao do grupo, 03/10/2026, registrada em docs/piloto/ESTADO.md antes desta
etapa): "disponivel" = acessivel a partir da regiao de qualquer forma (In-Region, Geo ou
Global; na pagina antiga, Yes ou Yes*). Celulas "Legacy" contam como disponivel.

Para cada par modelo x regiao fora dos EUA:
    U  primeiro dia com captura que mostra o par disponivel
    L  ultimo dia anterior a U com captura informativa que mostra o par indisponivel
       (modelo fora da pagina conta como indisponivel em todas as regioes)
    L_ef = max(L, dia anterior ao anuncio): o modelo nao pode chegar antes de existir
    largura = U - L_ef, em dias. A data real esta em (L_ef, U] (censura intervalar).
Se uma fonte datada (etapa 2) cai dentro de (L_ef, U], a data e exata (largura 0). Se cai
fora, o par e marcado com conflito e o intervalo e mantido.

Entradas:  dados/intermediario/piloto_{cdx,presenca,modelos,eventos_datados}.csv
Saidas:    dados/intermediario/piloto_eventos.csv
           resultados/tabelas/piloto_precisao.md
"""
import csv
import statistics
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
INTER = RAIZ / "dados" / "intermediario"
TABELAS = RAIZ / "resultados" / "tabelas"
FIM_JANELA = date(2026, 6, 30)

# Regioes da AWS por pais, para os posts do blog que nomeiam so o pais. A data do post so
# e aceita se cair dentro do intervalo das capturas, o que confere o mapeamento.
PAIS = {
    "Japan": ["ap-northeast-1", "ap-northeast-3"],
    "Australia": ["ap-southeast-2", "ap-southeast-4"],
    "Canada": ["ca-central-1", "ca-west-1"],
    "UAE": ["me-central-1"], "Bahrain": ["me-south-1"],
    "Middle East": ["me-central-1", "me-south-1"],
    "New Zealand": ["ap-southeast-6"],
    "India": ["ap-south-1", "ap-south-2"],
}


def d(s):
    s = s.replace("-", "")
    return date(int(s[:4]), int(s[4:6]), int(s[6:8]))


def ler(nome):
    with open(INTER / nome, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def observacoes():
    """{(modelo, regiao): {dia: True/False}} pela definicao do grupo (qualquer forma)."""
    por_digest = defaultdict(list)
    for r in ler("piloto_presenca.csv"):
        por_digest[(r["pagina"], r["digest"])].append(r)
    obs = defaultdict(dict)
    modelos = {r["modelo"] for r in ler("piloto_modelos.csv")}
    regioes_vistas = defaultdict(set)
    for r in ler("piloto_presenca.csv"):
        if r["regiao"] != "*":
            regioes_vistas[r["modelo"]].add(r["regiao"])
    for c in ler("piloto_cdx.csv"):
        dia = d(c["dia"])
        linhas = por_digest.get((c["pagina"], c["digest"]), [])
        if not linhas or any(x["situacao"] == "sem_info" for x in linhas):
            continue
        hoje = defaultdict(lambda: None)
        for x in linhas:
            if x["tipo"] == "so_cross_region":
                continue  # ja contido em "qualquer"
            if x["situacao"] == "modelo_ausente":
                for reg in regioes_vistas[x["modelo"]]:
                    hoje[(x["modelo"], reg)] = hoje[(x["modelo"], reg)] or False
            elif x["regiao"] != "*":
                k = (x["modelo"], x["regiao"])
                hoje[k] = bool(hoje[k]) or x["situacao"] == "presente"
        for k, v in hoje.items():
            if k[0] in modelos:
                anterior = obs[k].get(dia)
                obs[k][dia] = v if anterior is None else (anterior or v)
    return obs


def datas_exatas():
    """{(modelo, regiao): [(data, url)]} das fontes datadas de disponibilidade."""
    ex = defaultdict(list)
    for e in ler("piloto_eventos_datados.csv"):
        if e["natureza"] != "disponibilidade" or "ambiguo" in e["modelo"] or e["modelo"].startswith("Claude (sem"):
            continue
        regs = []
        for item in filter(None, e["regioes"].split(";")):
            regs += PAIS.get(item[5:], []) if item.startswith("pais:") else [item]
        for reg in set(regs):
            ex[(e["modelo"], reg)].append((d(e["data"]), e["url"]))
    return ex


def main():
    anuncio = {r["modelo"]: d(r["data_anuncio"]) for r in ler("piloto_modelos.csv")}
    obs, exatas = observacoes(), datas_exatas()
    eventos = []
    for (m, reg), serie in sorted(obs.items()):
        if reg.startswith("us-"):
            continue
        dias = sorted(serie)
        U = next((x for x in dias if serie[x]), None)
        antes = [x for x in dias if (U is None or x < U) and serie[x] is False]
        L = antes[-1] if antes else None
        piso = anuncio[m] - timedelta(days=1)
        truncado = U is not None and L is None and U <= piso
        L_ef = max(L, piso) if L else piso
        censurado = U is None
        largura = (U - L_ef).days if U else None
        data_exata, origem, conflito = "", "wayback", ""
        for dt, url in sorted(exatas.get((m, reg), [])):
            if U and L_ef < dt <= U:
                data_exata, origem, largura = dt.isoformat(), url, 0
                break
            conflito = f"{dt.isoformat()} fora de ({L_ef}, {U}]" if U else f"{dt.isoformat()} sem chegada nas capturas"
        defas = None
        if U:
            meio = date.fromisoformat(data_exata) if data_exata else L_ef + (U - L_ef) / 2
            defas = (meio - anuncio[m]).days
        eventos.append({
            "modelo": m, "regiao": reg, "tipo": "qualquer",
            "L": L_ef.isoformat() if U else (dias[-1].isoformat() if dias else ""),
            "U": U.isoformat() if U else "", "largura_dias": "" if largura is None else largura,
            "data_exata": data_exata, "origem": origem,
            "truncado_esquerda": "sim" if truncado else "nao",
            "censurado": "sim" if censurado else "nao", "conflito": conflito,
            "defasagem_dias_ponto_medio": "" if defas is None else defas,
            "periodo": str(anuncio[m].year)})
    with open(INTER / "piloto_eventos.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(eventos[0]))
        w.writeheader()
        w.writerows(eventos)

    def resumo(grupo):
        ev = [e for e in grupo if e["censurado"] == "nao"]
        larg = [e["largura_dias"] for e in ev]
        wb = [e["largura_dias"] for e in ev if not e["data_exata"]]
        dfs = [e["defasagem_dias_ponto_medio"] for e in ev]
        q = lambda v, p: sorted(v)[min(len(v) - 1, int(p * len(v)))] if v else "-"
        return [len(grupo), len(ev),
                f"{100 * sum(bool(e['data_exata']) for e in ev) / len(ev):.0f}%" if ev else "-",
                statistics.median(larg) if larg else "-", q(larg, 0.9),
                statistics.median(wb) if wb else "-",
                sum(e["truncado_esquerda"] == "sim" for e in grupo),
                sum(e["censurado"] == "sim" for e in grupo),
                sum(bool(e["conflito"]) for e in grupo),
                statistics.median(dfs) if dfs else "-"]

    cab = ["Grupo", "Pares", "Eventos", "% data exata", "Mediana largura (d)", "P90 largura (d)",
           "Mediana só Wayback (d)", "Truncados", "Censurados", "Conflitos", "Mediana defasagem (d)"]
    linhas = [["**Total**"] + resumo(eventos)]
    for p in ("2024", "2025", "2026"):
        linhas.append([f"Lançados em {p}"] + resumo([e for e in eventos if e["periodo"] == p]))
    for m in anuncio:
        linhas.append([m] + resumo([e for e in eventos if e["modelo"] == m]))

    TABELAS.mkdir(parents=True, exist_ok=True)
    md = ["# Piloto do desfecho: precisão da data de chegada", "",
          "Gerado por `src/tratamento/piloto_intervalos.py`. Regiões fora dos EUA, 5 modelos Claude no",
          "Amazon Bedrock, definição do grupo: acessível de qualquer forma, Legacy conta.",
          "Largura = dias do intervalo (L, U] em que a chegada aconteceu; 0 quando há data exata.",
          "Defasagem = dias entre o anúncio e o ponto médio do intervalo (ou a data exata).", "",
          "| " + " | ".join(cab) + " |", "|" + "---|" * len(cab)]
    md += ["| " + " | ".join(str(c) for c in l) + " |" for l in linhas]
    md += ["", "Critério registrado antes da coleta: mediana da largura ≤ 30 dias → a pergunta",
           "regional segue; > 30 dias, ou mais da metade dos pares truncados/sem informação → a",
           "pergunta de países vira a principal."]
    (TABELAS / "piloto_precisao.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print(" | ".join(cab))
    for l in linhas:
        print(" | ".join(str(c) for c in l))
    conf = [e for e in eventos if e["conflito"]]
    print(f"\nconflitos ({len(conf)}):")
    for e in conf[:12]:
        print(f"  {e['modelo']:21s} {e['regiao']:15s} {e['conflito']}")
    print("\nsaidas -> dados/intermediario/piloto_eventos.csv, resultados/tabelas/piloto_precisao.md")


if __name__ == "__main__":
    main()
