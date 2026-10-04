# Exercício 3 — Fichamento de artigos científicos

Estado em 03/10/2026: **documento completo, falta revisão humana e o link do Overleaf.**

| Arquivo | O que é |
|---|---|
| `ENTREGAR-Exercicio3-Fichamento.pdf` | PDF de entrega (18 p.), gerado de `latex/main.tex` com biblatex-abnt e biber |
| `latex/` | Fonte: capa, seleção, 3 fichamentos, quadro, síntese, `.bib` |
| `Declaracao-uso-IA.pdf` | Declaração de uso de IA **separada do documento**, por orientação do professor (fonte em `declaracao-ia/`) |
| `Exercicio3-Fichamento.docx` | Versão Word com o mesmo conteúdo do PDF (cópia de trabalho; a entrega oficial é o PDF do LaTeX) |
| `overleaf-exercicio3.zip` | Os mesmos `.tex` e `.bib`, prontos para subir no Overleaf |
| `artigos/` | Os três artigos que vão junto com o PDF |
| `revisao/checar_fichamento.py` | Confere citações, páginas e números de cada fichamento contra o PDF do artigo |

Distribuição: Ahmed e Wahed (2020) → Eduardo; McElheran et al. (2024) e Knez (2023) → Pedro.

## Pendências antes de entregar

1. ~~Link do projeto LaTeX~~ — resolvido em 04/10/2026: https://www.overleaf.com/read/rpywrfftkqyv#70ad2e
   (na capa). Ao editar no Overleaf, subir também o `latex/main.tex` atualizado.
2. ~~PDF publicado do McElheran~~ — resolvido em 04/10/2026: `artigos/mcelheran2024.pdf` é a versão
   da editora, e as páginas do Fichamento 2 (375–415) foram reconferidas com o script.
3. **Revisão pelos autores.** O texto foi redigido com o Claude, e a declaração de IA diz isso.
   Cada um deve ler o próprio fichamento contra o artigo e ajustar a declaração se fizer
   mudanças.
4. **Etapa 7 (revisão cruzada)** não foi feita. É do roteiro sugerido, não da entrega.

## Como regenerar o .docx depois de editar os .tex

```
python3 revisao/tex2html.py latex /tmp/ex3.html && python3 revisao/html2docx.py /tmp/ex3.html Exercicio3-Fichamento.docx
```

## Como conferir

```
python3 revisao/checar_fichamento.py latex/fichamento-1.tex artigos/ahmed2020.pdf 1
python3 revisao/checar_fichamento.py latex/fichamento-2.tex artigos/mcelheran2024.pdf 375
python3 revisao/checar_fichamento.py latex/fichamento-3.tex artigos/knez2023.pdf 1171
```

Os números que o script aponta no Fichamento 1 vêm das Tabelas 2 e 4 do Ahmed, que são imagens no
PDF. Foram conferidos visualmente.
