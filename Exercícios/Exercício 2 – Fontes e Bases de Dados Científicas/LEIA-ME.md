# Exercício 2 — Fontes e Bases de Dados Científicas

Estado: **rascunho completo, pendente de três ações do Pedro.**

## Arquivos

| Arquivo | O que é |
|---|---|
| `fontes-bases.tex` | Documento principal. Capa + 11 seções, cobrindo os 8 passos da oficina |
| `log-busca.csv` | Planilha de registro. 27 linhas, 3 marcadas `PENDENTE` |
| `buscas.py` | Reproduz as consultas das três bases abertas |

## O que falta

### 1. Criar o projeto no Overleaf e inserir o link

**O documento compila.** Foi gerado localmente com `tectonic` (instalado via Homebrew,
sem sudo), em 9 páginas, sem nenhum erro e sem nenhuma caixa vazando a margem. O
`fontes-bases.pdf` no repositório é essa compilação.

Falta apenas o link, que é o critério de entrega:

1. Criar projeto em branco no Overleaf e subir `fontes-bases.tex`.
2. Menu → Compiler → **pdfLaTeX**. Não precisa de biber: o documento não usa `biblatex`.
3. Compilar duas vezes, para o sumário assentar.
4. Substituir `[INSERIR AQUI O LINK DO OVERLEAF]` pelo endereço real e recompilar.
5. Configurar o link como **"Anyone with this link can view"**.

Para recompilar aqui depois de editar:

```
tectonic -X compile fontes-bases.tex
```

O Overleaf usa pdfLaTeX e o tectonic usa XeTeX. O documento foi escrito para funcionar nos
dois, mas conferir no PDF do Overleaf se o sumário e as tabelas saíram iguais.

O placeholder está dentro de uma caixa vermelha com o título "PREENCHER ANTES DE ENTREGAR",
justamente porque no Exercício 1 ele passou batido e foi parar no PDF entregue.

### 2. Rodar Scopus, ACM DL e IEEE Xplore com o acesso CAFe

As expressões já estão traduzidas para a sintaxe de cada uma, na seção 8 do documento.
Basta colar, rodar e anotar. Depois, preencher as três linhas `PENDENTE` do `log-busca.csv`
e acrescentar os números à seção 7.

Cuidados que valem ponto:

- **ACM DL:** conferir em *View Query Syntax* antes de anotar o número. Termos na mesma
  linha são combinados com `OR` por padrão, linhas diferentes com `AND`.
- **Scopus:** agrupar tudo com parênteses. A Elsevier mudou a precedência dos booleanos, com
  implantação concluída no início de 2026.
- **IEEE:** usar *Command Search*; por padrão busca só metadados.

Se rodar a Scopus, ela é a base de calibração que a apostila sugere — e provavelmente vai
devolver números bem menores que os da OpenAlex, porque o escopo é curado. Vale registrar
essa diferença como observação.

### 3. Abrir os cinco artigos do conjunto-controle

A apostila é explícita: *"Todo artigo do seu conjunto-controle precisa ser aberto e visto
por você."* Os cinco têm DOI verificado contra Crossref, DataCite e a API do arXiv, e os
resumos foram lidos via API — mas isso não é o mesmo que abrir. Todos são de acesso aberto
ou acessíveis pelo DOI.

## O achado central, caso o professor pergunte

Nenhuma expressão única é ao mesmo tempo capaz de recuperar os cinco artigos do
conjunto-controle e de devolver um volume triável. A causa foi diagnosticada, não suposta:
dois dos cinco artigos só são alcançados por termos de território e governança, e os outros
três só por termos da família *divide* — são literaturas diferentes.

Foi verificado que o volume não era artefato de sintaxe: a OpenAlex respeita frase exata
(`"artificial intelligence"` devolve 327.044 no título contra 154 da frase invertida).

A saída foi declarar **duas linhas de busca**, cada uma triável, cuja união recupera 5/5.

## Observações sobre o enunciado

- A oficina diz **trio**; o projeto é dupla. A capa traz Pedro e Eduardo.
- A apostila não lista a **OpenAlex** entre as bases. Ela foi usada como base de calibração
  por ser a única indexadora de acesso irrestrito disponível, e isso está declarado na
  seção 10 do documento. A SBC OpenLib cobre a exigência de biblioteca digital.
