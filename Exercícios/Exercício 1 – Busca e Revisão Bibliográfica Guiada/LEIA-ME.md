# Exercício 1 — Busca e Revisão Bibliográfica Guiada

Estado: **texto completo, mas a entrega ainda não cumpre o critério 8.**

## Autoria

O trabalho e assinado por **Pedro Dias Soares e Eduardo Velloso Landeiro**.

Registro de divergencia: o `PROMPT-execucao.md`, que originou este exercicio,
afirma na linha 14 que se trata de atividade individual. A decisao de assinar em
dupla foi tomada depois, em 20/09/2026. Se o enunciado do professor exigir
entrega individual, e o `\author` do `.tex` que precisa voltar atras.

## Arquivos

| Arquivo | O que é |
|---|---|
| `revisao.tex` | Documento principal. Sete seções na ordem exigida, mais "Link do projeto LaTeX" |
| `referencias.bib` | 12 entradas, todas com DOI verificado |
| `log-busca.csv` | 21 registros: 17 expressões de recuperação e 4 linhas de outras bases |
| `verificacao-referencias.md` | Conferência referência a referência |
| `PROMPT-execucao.md` | Prompt que originou este trabalho |
| `Revisao-Bibliografica.pdf` | PDF antigo — **não serve para entrega**, ver abaixo |
| `Revisao-Bibliografica.docx` | Versão em Word, origem do PDF acima |

## O problema mais sério

**Nenhum dos dois PDFs existentes foi gerado em LaTeX.** Verificado nos metadados
em 17/09/2026:

| Arquivo | Producer | Páginas apaisadas |
|---|---|---|
| `Revisao-Bibliografica.pdf` (nesta pasta) | LibreOffice Writer | nenhuma |
| `../Revisao-Bibliografica.pdf` (pasta acima) | macOS Quartz (Word/Preview) | nenhuma |

O `revisao.tex` usa `\begin{landscape}` para as tabelas comparativas, o que obriga
páginas com `/Rotate 90`. Nenhum dos dois PDFs tem. É prova de que não saíram deste
`.tex`.

O critério 8 pede **"entrega do PDF gerado em LaTeX com o respectivo link para o
arquivo-fonte"**. Como está, não cumpre — e o professor confere isso abrindo as
propriedades do arquivo.

**A correção é compilar o `revisao.tex` no Overleaf** e entregar aquele PDF. Isso
resolve o critério 8 e produz o link na mesma operação.

## Por que não dá para compilar localmente

O estilo ABNT exige o biber, e diz isso de forma literal:

```
abnt.bbx:21: Package biblatex Error: Biber backend is required by style.
l.21 \RequireBiber[3]
```

Testado `backend=bibtex` (que o tectonic traz embutido): recusado na linha 21 do
próprio `abnt.bbx`. E o biber não instala nesta máquina — é um Mac Intel, e o
Homebrew parou de distribuir binário para x86_64; o build do zero falha num módulo
Perl XS.

Se quiser resolver local algum dia, o caminho é o BasicTeX, que traz o biber. Precisa
da sua senha:

```
brew install --yes --cask basictex && sudo tlmgr install biber biblatex-abnt
```

## Correções já aplicadas no `revisao.tex` (17/09/2026)

Validadas por compilação-proxy (`authoryear`+`bibtex`, que aproxima a largura das
citações ABNT) — 11 páginas, 3 apaisadas, tabelas íntegras.

1. **7 travessões literais `—` → `---`.** O XeTeX não representa `—` na fonte EC
   ("Missing character"); o pdfLaTeX representa. Era incompatibilidade latente,
   invisível no Overleaf. O `---` funciona nos dois, com saída idêntica.
2. **`\texttt{verificacao-referencias.md}`** vazava 62pt — nome de arquivo
   monoespaçado inquebrável. Envolvido em `sloppypar`.
3. **Parágrafo "Fonte de dados"** vazava 33pt, denso de `\cite`. Sob ABNT as citações
   são mais longas, então pioraria. Também em `sloppypar`.

## O que falta

### 1. Compilar no Overleaf e inserir o link

1. Criar projeto em branco e subir `revisao.tex` e `referencias.bib`.
2. Menu → Compiler → **pdfLaTeX**.
3. Compilar, rodar o **biber**, compilar mais duas vezes.
4. Substituir `[INSERIR AQUI O LINK DO OVERLEAF]` pelo endereço real e recompilar.
5. Configurar como **"Anyone with this link can view"** — sem isso o critério 8 não
   é cumprido.

**Conferir no PDF antes de exportar:** nenhuma citação saindo como `[?]`; a lista de
referências preenchida; as três tabelas comparativas em retrato, com as sete colunas exigidas distribuídas entre elas.

### 2. Ler os dez textos integralmente

A tabela comparativa foi montada a partir de **resumos e metadados**, não da leitura
integral. Isso está declarado na seção 3.6 do documento e assinalado com *(inferida)*
nas células de limitação que vieram do desenho do estudo. Revisar sobretudo as colunas
*Principais resultados* e *Limitações observadas*. Todos os dez são abertos ou
acessíveis pelo DOI.

## Limitação de busca a declarar, se perguntado

**Scopus e Web of Science não foram consultadas diretamente** — exigem assinatura
institucional. A cobertura foi aproximada pela OpenAlex. Vale repetir as expressões da
seção 3.3 com o acesso da PUC Minas (CAFe) e acrescentar as linhas ao `log-busca.csv`.

A busca direta no SciELO não respondeu do ambiente usado; a cobertura em português
saiu do filtro de idioma da OpenAlex, que indexa periódicos SciELO.
