"""Gera .docx (WordprocessingML puro, sem dependências) a partir do HTML simples de tex2html.py."""
import re, sys, zipfile, html
from xml.sax.saxutils import escape

src, out = sys.argv[1], sys.argv[2]
H = open(src, encoding="utf-8").read()
H = H[H.index("<body>") + 6:H.index("</body>")]

def runs(frag, size=None, bold=False):
    """Converte HTML inline (<b>, <i>, <tt>, <br>) em runs do Word."""
    xml, b, i, tt = [], bold, False, False
    for tok in re.split(r"(<[^>]+>)", frag):
        if not tok:
            continue
        t = tok.lower()
        if t.startswith("<b>"): b = True; continue
        if t.startswith("</b>"): b = bold; continue
        if t.startswith("<i>"): i = True; continue
        if t.startswith("</i>"): i = False; continue
        if t.startswith("<tt>"): tt = True; continue
        if t.startswith("</tt>"): tt = False; continue
        if t.startswith("<br"): xml.append("<w:r><w:br/></w:r>"); continue
        if t.startswith("<"): continue
        text = html.unescape(tok)
        rpr = ""
        if b: rpr += "<w:b/>"
        if i: rpr += "<w:i/>"
        if tt: rpr += '<w:rFonts w:ascii="Courier New" w:hAnsi="Courier New"/>'
        if size: rpr += f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>'
        xml.append(f'<w:r><w:rPr>{rpr}</w:rPr><w:t xml:space="preserve">{escape(text)}</w:t></w:r>')
    return "".join(xml)

def para(frag, style=None, align=None, size=None, brk=False, bold=False):
    ppr = ""
    if style: ppr += f'<w:pStyle w:val="{style}"/>'
    if brk: ppr += "<w:pageBreakBefore/>"
    if align: ppr += f'<w:jc w:val="{align}"/>'
    return f"<w:p><w:pPr>{ppr}</w:pPr>{runs(frag, size, bold)}</w:p>"

body = []
for m in re.finditer(r"<(h1|h2|p|table)([^>]*)>(.*?)</\1>", H, re.S):
    tag, attrs, inner = m.groups()
    brk = "page-break-before" in attrs
    center = "text-align:center" in attrs
    size = None
    fs = re.search(r"font-size:(\d+)pt", attrs)
    if fs: size = int(fs.group(1)) * 2
    if tag == "h1":
        body.append(para(inner, "Heading1", brk=brk))
    elif tag == "h2":
        body.append(para(inner, "Heading2"))
    elif tag == "p":
        body.append(para(inner, align="center" if center else ("left" if "text-align:left" in attrs else "both"), size=size))
    else:
        rows = re.findall(r"<tr>(.*?)</tr>", inner, re.S)
        tbl = ['<w:tbl><w:tblPr><w:tblW w:w="5000" w:type="pct"/><w:tblBorders>'
               + "".join(f'<w:{s} w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
                         for s in ["top", "left", "bottom", "right", "insideH", "insideV"])
               + "</w:tblBorders></w:tblPr>"]
        for k, r in enumerate(rows):
            cells = re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", r, re.S)
            tr = "<w:tr>" + ("<w:trPr><w:tblHeader/></w:trPr>" if k == 0 else "")
            for j, c in enumerate(cells):
                tr += (f'<w:tc><w:tcPr><w:tcW w:w="{1100 if j == 0 else 1300}" w:type="pct"/></w:tcPr>'
                       + para(c, size=18, bold=(k == 0 or j == 0)) + "</w:tc>")
            tbl.append(tr + "</w:tr>")
        tbl.append("</w:tbl>")
        body.append("".join(tbl))

sect = ('<w:sectPr><w:pgSz w:w="11906" w:h="16838"/>'
        '<w:pgMar w:top="1418" w:right="1418" w:bottom="1418" w:left="1418" w:header="709" w:footer="709" w:gutter="0"/></w:sectPr>')
NS = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'
document = f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document {NS}><w:body>{"".join(body)}{sect}</w:body></w:document>'
styles = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:styles {NS}>
<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/><w:sz w:val="24"/><w:szCs w:val="24"/><w:lang w:val="pt-BR"/></w:rPr></w:rPrDefault>
<w:pPrDefault><w:pPr><w:spacing w:after="120" w:line="300" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults>
<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/></w:style>
<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:pPr><w:keepNext/><w:spacing w:before="240" w:after="160"/><w:outlineLvl w:val="0"/></w:pPr><w:rPr><w:b/><w:sz w:val="32"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:pPr><w:keepNext/><w:spacing w:before="200" w:after="80"/><w:outlineLvl w:val="1"/></w:pPr><w:rPr><w:b/><w:sz w:val="26"/></w:rPr></w:style>
</w:styles>'''
ct = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/></Types>'''
rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>'''
drels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/></Relationships>'''
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("[Content_Types].xml", ct); z.writestr("_rels/.rels", rels)
    z.writestr("word/document.xml", document); z.writestr("word/styles.xml", styles)
    z.writestr("word/_rels/document.xml.rels", drels)
print("ok", out, len(body), "blocos")
