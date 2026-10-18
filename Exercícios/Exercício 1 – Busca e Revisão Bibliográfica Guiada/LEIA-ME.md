# Exercício 1 — Busca e Revisão Bibliográfica Guiada

Estado: **PDF de entrega gerado com biblatex (03/10/2026). Falta atualizar o Overleaf
e ler os dez textos integralmente.**

## Autoria

O trabalho e assinado por **Pedro Dias Soares e Eduardo Velloso Landeiro**.

Registro de divergencia: o `PROMPT-execucao.md`, que originou este exercicio,
afirma na linha 14 que se trata de atividade individual. A decisao de assinar em
dupla foi tomada depois, em 20/09/2026. Se o enunciado do professor exigir
entrega individual, e o `\author` do `.tex` que precisa voltar atras.

## Arquivos

| Arquivo | O que é |
|---|---|
| `ENTREGAR-Exercicio1-Revisao-Bibliografica.pdf` | **PDF de entrega.** Gerado de `revisao.tex`, com biblatex-abnt e biber |
| `revisao.tex` | **Fonte da entrega.** Usa `biblatex` com `style=abnt`, como o enunciado exige |
| `referencias.bib` | 12 entradas, todas com DOI verificado |
| `revisao-leve.tex` | Reserva sem biblatex, com referências escritas à mão. **Não atende** ao "Use o pacote biblatex" do enunciado; só serve se nada mais compilar |
| `log-busca.csv` | 21 registros: 17 expressões de recuperação e 4 linhas de outras bases |
| `verificacao-referencias.md` | Conferência referência a referência |
| `PROMPT-execucao.md` | Prompt que originou este trabalho |
| `Revisao-Bibliografica.pdf` / `.docx` | Versão antiga em Word. **Não serve para entrega** (não saiu de LaTeX e tem o link vazio) |

## Correções de 03/10/2026

1. **A entrega voltou a usar biblatex.** O PDF anterior (commit 2eaf9d4) saiu do
   `revisao-leve.tex`, sem biblatex, embora o enunciado diga "Use o pacote biblatex".
2. **"Knez (2023) chegam perto"** virou "chega perto"; faltava a crase em "aplicando à
   documentação".
3. **O artigo da Liinc aparecia de três formas** (Guimarães Furtado e Evangelista Cunha,
   Furtado e Cunha, Furtado e Evangelista). Padronizado pela ABNT (NBR 6023:2018,
   8.1.1.1), que entra pelo último sobrenome: FURTADO; CUNHA. A Crossref registra
   "Guimarães Furtado"/"Evangelista Cunha" como sobrenome; a divergência está anotada
   no `.bib`.
4. **As expressões de busca saíam sem o espaço depois das aspas** (`"digital divide"OR`).
   Causa: o babel em português torna `"` um caractere ativo, e ele engolia o espaço.
   Corrigido com `shorthands=off`.
5. `useprefix=true` no biblatex, para sair VAN DEURSEN; VAN DIJK (e não DEURSEN … van),
   e `location` no Amos, que saía com [S.l.].

## Como o PDF foi compilado

O Overleaf gratuito estourou o tempo três vezes com a versão biblatex (commit 20abc16).
Por isso o PDF foi compilado nesta máquina: `tectonic` 0.17 (biblatex 3.17) com o
**biber 2.17**, a única versão compatível, baixada do projeto oficial no SourceForge
para a pasta temporária da sessão, sem instalação no sistema. Para recompilar, é
preciso de novo um biber 2.17 no PATH:

```
PATH="/caminho/do/biber-2.17:$PATH" tectonic -X compile revisao.tex
```

## O que falta

### 1. Atualizar o projeto do Overleaf

O link impresso no PDF é https://www.overleaf.com/read/qbcvqyhkcymy. O projeto ainda deve
conter a versão leve. Substituir os arquivos pelos do `overleaf-exercicio1.zip`
(`revisao.tex` + `referencias.bib`), para que o fonte do link seja o mesmo do PDF.
Se o Overleaf voltar a estourar o tempo, o fonte continua visível pelo link, que é
o que o critério 8 pede. O enunciado aceita também o **Prism** como plataforma.

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
