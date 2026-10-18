# Exercício 2 — Fontes e Bases de Dados Científicas

Estado: **rascunho completo, pendente de três ações do Pedro.**

## Arquivos

| Arquivo | O que é |
|---|---|
| `fontes-bases.tex` | Documento principal. Capa + 11 seções, cobrindo os 8 passos da oficina |
| `log-busca.csv` | Planilha de registro. 30 linhas, 6 marcadas `PENDENTE` (Linha A e Linha B em cada base assinada) |
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

As expressões já estão traduzidas para a sintaxe de cada uma, na seção 8 do documento,
**uma para a Linha A e outra para a Linha B**. Rodar as duas em cada base, conferindo
quantos dos cinco artigos do conjunto-controle cada uma recupera: só a união das duas
cobre o controle inteiro. Depois, preencher as seis linhas `PENDENTE` do `log-busca.csv`
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

## Correções de 03/10/2026

1. **Tabela de versões.** v4 e v5 apareciam como posteriores à revisão do
   conjunto-controle, mas ainda eram medidas contra o conjunto inicial: o log registra
   que v4 "recupera Knez" e que v6 é a "primeira versão contra o conjunto-controle
   revisado". A tabela ganhou um grupo próprio para v4–v5, e a linha `rev` do log foi
   movida para entre v5 e v6.
2. **Traduções para as bases assinadas.** Scopus, ACM e IEEE traziam só a Linha A, e com
   termos a menos, o que recuperaria no máximo 3/5. Agora as duas linhas estão traduzidas,
   com os mesmos termos das expressões finais da OpenAlex. Na ACM, os dois blocos passaram
   a ser buscados no resumo, como no arXiv.
3. **Aspas.** As expressões saíam como `"digital divide"OR`, sem o espaço: o babel em
   português torna `"` ativo. Corrigido com `shorthands=off` (e `brazil` virou
   `brazilian`, a forma não obsoleta).

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
