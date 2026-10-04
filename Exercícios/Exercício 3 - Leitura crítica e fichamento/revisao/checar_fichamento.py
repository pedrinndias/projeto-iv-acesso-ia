"""
Etapa 6R do PROMPT-exercicio3-fichamento.md: verificações determinísticas de um fichamento
contra o texto do artigo. Só aponta; não reescreve nada.

Uso:
    python3 revisao/checar_fichamento.py latex/fichamento-1.tex artigos/ahmed2020.pdf [primeira_pagina]

primeira_pagina = número impresso da 1ª página do PDF (ex.: 375 em McElheran et al., 1171 em
Knez); padrão 1. Serve para conferir as páginas das citações diretas.

Verifica:
 1. os 12 itens existem e não estão vazios; autoria preenchida
 2. citação entre aspas existe literalmente no artigo e tem página, que confere
 3. números dos itens 6 e 8 aparecem no artigo
 4. trechos de 8+ palavras idênticos ao artigo fora de aspas
 5. frases dos itens 10 e 12 sem âncora (Tabela, Figura, Seção, página)
 6. item 5 diz se a hipótese é explícita ou reconstruída; item 12 tem auditoria e exame de afirmação
"""
import re
import sys
from pathlib import Path

ITENS = ["Referência bibliográfica", "Tema do artigo", "Problema investigado",
         "Objetivo do trabalho", "Hipótese ou pressuposto", "Base de dados ou corpus",
         "Metodologia ou abordagem", "Principais resultados", "Conclusões dos autores",
         "Limitações do estudo", "Contribuições", "Avaliação crítica"]
ANCORA = re.compile(r"Tabela|Table|Figura|Figure|Fig\.|Se[çc][ãa]o|Section|Ap[êe]ndice|"
                    r"Appendix|Eq\.|equa[çc][ãa]o|\bp\.\s*\d|\bpp\.\s*\d", re.I)
ASPAS = re.compile(r"``(.+?)''|“(.+?)”|\\enquote\{(.+?)\}|\"(.+?)\"", re.S)
PAGINA = re.compile(r"^\s*[,;]?\s*\(?\s*p\.?\s*~?\s*(\d+)")


def norm(s):
    s = s.replace("\u00ad", "").replace("ﬁ", "fi").replace("ﬂ", "fl")
    s = re.sub(r"-\s*\n\s*", "", s)
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip().lower()


def ler_artigo(caminho):
    if caminho.suffix == ".txt":
        return caminho.read_text(encoding="utf-8").split("\f")
    from pypdf import PdfReader
    return [p.extract_text() or "" for p in PdfReader(str(caminho)).pages]


def tex_para_texto(s):
    s = re.sub(r"(?<!\\)%.*", "", s)
    s = re.sub(r"\\(?:full|text|paren|auto)?cite\w*\{[^}]*\}", "", s)
    s = re.sub(r"\\(?:textit|emph|textbf|texttt|textsc)\{([^}]*)\}", r"\1", s)
    s = s.replace("\\%", "%").replace("~", " ").replace("---", "—").replace("--", "–")
    s = re.sub(r"\\noindent|\\par\b|\\\\", " ", s)
    return s


def itens(tex):
    partes = re.split(r"\\subsection\*?\{\s*(\d+)\.\s*[^}]*\}", tex)
    return {int(partes[i]): partes[i + 1] for i in range(1, len(partes) - 1, 2)}


def numeros(s):
    for m in re.finditer(r"\d[\d.,]*\d%?|\d%?", s):
        t = m.group().rstrip("%").rstrip(".,")
        if len(re.sub(r"\D", "", t)) < 2:
            continue
        variantes = {t, t.replace(".", ""), t.replace(".", ","), t.replace(",", "."),
                     t.replace(".", "").replace(",", ".")}
        if re.fullmatch(r"\d{1,3}(\.\d{3})+", t):
            variantes.add(t.replace(".", ","))
        yield m.group(), variantes


def main():
    fich, art = Path(sys.argv[1]), Path(sys.argv[2])
    pag0 = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    bruto = fich.read_text(encoding="utf-8")
    paginas = [norm(p) for p in ler_artigo(art)]
    artigo = " ".join(paginas)
    texto = tex_para_texto(bruto)
    it = itens(texto)
    print(f"# {fich.name} × {art.name} ({len(paginas)} páginas, 1ª = p. {pag0})")

    print("\n[1] Estrutura")
    m = re.search(r"Autoria do fichamento:\}?\s*([^\n]+)", texto)
    print("  autoria:", m.group(1).strip() if m else "AUSENTE")
    for n, nome in enumerate(ITENS, 1):
        corpo = re.sub(r"\s+", " ", it.get(n, "")).strip()
        if n not in it:
            print(f"  item {n} ({nome}): AUSENTE")
        elif len(corpo) < 40 and n != 1:
            print(f"  item {n} ({nome}): vazio ou curto demais ({len(corpo)} caracteres)")

    print("\n[2] Citações diretas")
    sem_aspas = texto
    achou = False
    for q in ASPAS.finditer(texto):
        achou = True
        cit = next(g for g in q.groups() if g)
        sem_aspas = sem_aspas.replace(q.group(), " ")
        alvo = norm(cit)
        pg = PAGINA.match(texto[q.end():q.end() + 25])
        onde = [i for i, p in enumerate(paginas) if alvo in p]
        if not onde:  # citação que atravessa a quebra de página
            onde = [i for i in range(len(paginas) - 1)
                    if alvo in paginas[i] + " " + paginas[i + 1]]
            onde += [i + 1 for i in onde]
        rot = f'"{cit[:50]}..."' if len(cit) > 50 else f'"{cit}"'
        if not onde:
            print(f"  NÃO ENCONTRADA no artigo: {rot}")
        elif not pg:
            print(f"  sem página: {rot} (está na p. {pag0 + onde[0]})")
        elif int(pg.group(1)) not in [pag0 + i for i in onde]:
            print(f"  página não confere: {rot} citada como p. {pg.group(1)}, está na p. {pag0 + onde[0]}")
    if not achou:
        print("  nenhuma citação direta")

    print("\n[3] Números dos itens 6 e 8 que não aparecem no artigo")
    falta = [orig for n in (6, 8) for orig, var in numeros(it.get(n, ""))
             if not any(v in artigo for v in var)]
    print("  " + (", ".join(falta) if falta else "nenhum"))

    print("\n[4] Trechos de 8+ palavras iguais ao artigo, fora de aspas")
    corpo = re.sub(r"\\\w+\*?(\{[^}]*\})?", " ", sem_aspas)
    pal = re.findall(r"\w+", norm(corpo))
    art_pal = re.findall(r"\w+", artigo)
    grams = {tuple(art_pal[i:i + 8]) for i in range(len(art_pal) - 7)}
    trechos, i = [], 0
    while i < len(pal) - 7:
        if tuple(pal[i:i + 8]) in grams:
            j = i + 8
            while j < len(pal) and tuple(pal[j - 7:j + 1]) in grams:
                j += 1
            trechos.append(" ".join(pal[i:j]))
            i = j
        else:
            i += 1
    print("\n".join(f"  {t[:120]}" for t in trechos) if trechos else "  nenhum")

    print("\n[5] Frases dos itens 10 e 12 sem âncora no artigo (conferir se são juízo)")
    soltas = []
    for n in (10, 12):
        frases = re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", it.get(n, "")).strip())
        soltas += [f"  item {n}: {f[:110]}" for f in frases if len(f) > 15 and not ANCORA.search(f)]
    print("\n".join(soltas[:10]) if soltas else "  nenhuma")

    print("\n[6] Exigências específicas")
    i5 = it.get(5, "").lower()
    print("  item 5 diz explícita/reconstruída:", "sim" if re.search(r"expl[íi]cit|reconstru", i5) else "NÃO")
    i12 = it.get(12, "")
    print("  item 12 cita figura ou tabela:", "sim" if re.search(r"Tabela|Figura|Table|Figure", i12) else "NÃO")
    print("  item 12 examina afirmação do resumo/conclusão:",
          "sim" if re.search(r"resumo|conclus|abstract", i12, re.I) else "NÃO")


if __name__ == "__main__":
    main()
