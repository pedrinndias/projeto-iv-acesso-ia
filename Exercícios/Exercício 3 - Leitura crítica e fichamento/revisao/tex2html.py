"""Converte os .tex do Exercício 3 num HTML simples, que o textutil do macOS transforma em .docx."""
import re
import sys
from pathlib import Path

D = Path(sys.argv[1])  # pasta latex/
OUT = Path(sys.argv[2])

REFS = {
    "ahmed2020": ("AHMED, Nur; WAHED, Muntasir. <b>The De-democratization of AI: Deep Learning and the "
                  "Compute Divide in Artificial Intelligence Research</b>. 2020. DOI: 10.48550/arXiv.2010.15581. "
                  "arXiv: 2010.15581 [cs.CY]. Disponível em: &lt;https://arxiv.org/abs/2010.15581&gt;. "
                  "Acesso em: 11 set. 2026."),
    "knez2023": ("KNEZ, Klemen. Technology diffusion and uneven development. <b>Journal of Evolutionary "
                 "Economics</b>, v. 33, n. 4, p. 1171–1195, 2023. DOI: 10.1007/s00191-023-00830-w."),
    "mcelheran2024": ("MCELHERAN, Kristina et al. AI adoption in America: Who, what, and where. <b>Journal of "
                      "Economics &amp; Management Strategy</b>, v. 33, n. 2, p. 375–415, 2024. "
                      "DOI: 10.1111/jems.12576."),
}
TEXTCITE = {"ahmed2020": "Ahmed e Wahed (2020)", "knez2023": "Knez (2023)",
            "mcelheran2024": "McElheran <i>et al.</i> (2024)"}

MATH = [
    (r"x = \alpha \cdot (\textrm{salário médio mundial}/\textrm{salário do país})",
     "<i>x</i> = α · (salário médio mundial / salário do país)"),
    (r"\exp[-(x_1^2-x_2^2)/(4Dt)]", "exp[−(<i>x</i>₁² − <i>x</i>₂²)/(4<i>Dt</i>)]"),
    (r"R^2 = 0{,}230", "R² = 0,230"), (r"R^2 = 0{,}474", "R² = 0,474"), (r"R^2", "R²"),
    (r"D = 0{,}00202", "<i>D</i> = 0,00202"), (r"D = 0{,}00318", "<i>D</i> = 0,00318"),
    (r"\alpha = 0{,}329", "α = 0,329"), (r"\alpha = 0{,}477", "α = 0,477"),
    (r"p < 0{,}001", "<i>p</i> &lt; 0,001"), (r"\alpha", "α"), (r"\Phi", "Φ"),
    (r"x=0", "<i>x</i> = 0"), ("-", "−"), ("D", "<i>D</i>"), ("x", "<i>x</i>"), ("t", "<i>t</i>"),
]


def math(m):
    s = re.sub(r"\s+", " ", m.group(1))
    for a, b in MATH:
        if s == a:
            return b
    raise SystemExit(f"math sem tradução: {s}")


def inline(s):
    s = re.sub(r"(?<!\\)%.*", "", s)
    s = re.sub(r"\$([^$]+)\$", math, s)
    s = re.sub(r"\\textcite\{(\w+)\}", lambda m: TEXTCITE[m.group(1)], s)
    s = re.sub(r"\\fullcite\{(\w+)\}", lambda m: REFS[m.group(1)], s)
    for _ in range(2):
        s = re.sub(r"\\textbf\{([^{}]*)\}", r"<b>\1</b>", s)
        s = re.sub(r"\\(?:emph|textit)\{([^{}]*)\}", r"<i>\1</i>", s)
        s = re.sub(r"\\texttt\{([^{}]*)\}", r"<tt>\1</tt>", s)
    s = s.replace("``", "“").replace("''", "”").replace("\\%", "%").replace("\\&", "&amp;")
    s = s.replace("\\_", "_").replace("--", "–").replace("~", " ")
    s = re.sub(r"\\noindent|\\smallskip|\\par\b", "", s)
    if "\\" in s:
        raise SystemExit(f"comando LaTeX sobrando: {s[:200]}")
    return re.sub(r"\s+", " ", s).strip()


def body(tex):
    html = []
    tex = re.sub(r"(?m)^\s*%.*\n", "", tex)
    for bloco in re.split(r"\n\s*\n", tex):
        bloco = bloco.strip()
        if not bloco:
            continue
        m = re.match(r"\\section\*?\{(.+)\}\s*(.*)", bloco, re.S)
        if m:
            html.append(f'<h1 style="page-break-before:always">{inline(m.group(1))}</h1>')
            bloco = m.group(2).strip()
            if not bloco:
                continue
        m = re.match(r"\\subsection\*?\{(.+?)\}\s*(.*)", bloco, re.S)
        if m:
            html.append(f"<h2>{inline(m.group(1))}</h2>")
            bloco = m.group(2).strip()
            if not bloco:
                continue
        esq = ' style="text-align:left"' if "\\fullcite" in bloco else ""
        html.append(f"<p{esq}>{inline(bloco)}</p>")
    return "\n".join(html)


def quadro(tex):
    linhas = tex[tex.index("\\endlastfoot") + len("\\endlastfoot"):tex.index("\\end{longtable}")]
    linhas = [l for l in re.split(r"\\\\\s*(?:\\addlinespace)?", linhas) if l.strip()]
    cab = ["", "Ahmed e Wahed (2020)", "McElheran et al. (2024)", "Knez (2023)"]
    out = ['<h1 style="page-break-before:always">Quadro comparativo</h1>',
           '<table border="1" cellpadding="4" cellspacing="0" style="border-collapse:collapse;font-size:9pt">',
           "<tr>" + "".join(f"<th>{c}</th>" for c in cab) + "</tr>"]
    for l in linhas:
        cels = [inline(c) for c in l.split("&")]
        out.append("<tr>" + "".join(f"<td valign='top'>{c}</td>" for c in cels) + "</tr>")
    out.append("</table>")
    return "\n".join(out)


main = (D / "main.tex").read_text(encoding="utf-8")
link = re.search(r"\\newcommand\{\\linkprojeto\}\{(.*)\}", main).group(1)
link = re.sub(r"\\url\{(.*)\}", r"\1", link).replace("\\#", "#")
capa = f"""
<p style="text-align:center">Pontifícia Universidade Católica de Minas Gerais<br>
Instituto de Ciências Exatas e Informática<br>Ciência de Dados e Inteligência Artificial</p>
<p>&nbsp;</p><p>&nbsp;</p>
<p style="text-align:center;font-size:18pt"><b>Fichamento de artigos científicos</b></p>
<p style="text-align:center">Tema do grupo: desigualdade geográfica no acesso a modelos de inteligência artificial generativa comercial</p>
<p style="text-align:center;font-size:10pt">Recorte: como a literatura empírica mede a desigualdade, entre lugares e organizações, no acesso à inteligência artificial e na adoção de tecnologias de fronteira</p>
<p>&nbsp;</p><p>&nbsp;</p>
<p style="text-align:center">Pedro Dias Soares<br>Eduardo Velloso Landeiro</p>
<p>&nbsp;</p><p>&nbsp;</p>
<p style="text-align:center">Projeto em Ciência de Dados IV, Prof. Rodrigo Richard Gomes<br>2º semestre de 2026</p>
<p style="text-align:center;font-size:10pt">Link do projeto LaTeX: {link}</p>
"""
partes = [capa]
for nome in ["selecao", "fichamento-1", "fichamento-2", "fichamento-3"]:
    partes.append(body((D / f"{nome}.tex").read_text(encoding="utf-8")))
partes.append(quadro((D / "quadro.tex").read_text(encoding="utf-8")))
partes.append(body((D / "sintese.tex").read_text(encoding="utf-8")))
refs = "".join(f'<p style="text-align:left">{REFS[k]}</p>' for k in ["ahmed2020", "knez2023", "mcelheran2024"])
partes.append(f'<h1 style="page-break-before:always">Referências</h1>{refs}')

OUT.write_text(f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Fichamento de artigos científicos</title>
<style>body{{font-family:'Times New Roman';font-size:12pt}} h1{{font-size:16pt}} h2{{font-size:13pt}}
p{{text-align:justify}}</style></head><body>
{''.join(partes)}
</body></html>""", encoding="utf-8")
print("ok", OUT)
