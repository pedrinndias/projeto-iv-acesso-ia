# Entrega 1 — auditoria e arquivos

O guia e o template oficial foram conferidos em 26/11/2026. A primeira minuta continha a estrutura do enunciado, mas usava capa própria, citações `natbib/plainnat`, matriz horizontal e um Apêndice C apenas de autoria. Ela também incluía uma pergunta, uma revisão e uma bibliografia produzidas com assistência de IA. O template oficial veda gerar esses três itens com IA. A minuta anterior está arquivada para rastreabilidade interna. A base editável é o ponto de partida para a versão acadêmica.

## Arquivos

| Local | Conteúdo |
|---|---|
| [PCDIV-Entrega1-Overleaf.zip](PCDIV-Entrega1-Overleaf.zip) | Pacote para **New Project → Upload Project**, com os três arquivos na raiz. |
| [overleaf/](overleaf/) | `main.tex`, `referencias.bib` e `puclogo.pdf` que correspondem ao ZIP. |
| [Demandas da disciplina](../../demandas/README.md) | Enunciado em Word, imagens da rubrica e guia do Overleaf. |
| [Template local adaptado](template-local/) | Fonte LaTeX do modelo e seus arquivos de apoio. |
| [Cópia local do template em PDF](material-interno/PCDIV-Entrega1-Modelo-Local.pdf) | Modelo LaTeX compilado. |
| [Prévia técnica em PDF](material-interno/PCDIV-Entrega1-Previa.pdf) | Compilação da base com os campos acadêmicos pendentes. |
| [material-interno/](material-interno/) | PDF, fonte, bibliografia, registro de conferência e prompt histórico da versão assistida anterior. |

## Resultado da auditoria

| Item | Minuta anterior | Base preparada |
|---|---|---|
| Capa, brasão e formatação | Identidade própria, sem o brasão do template. | Capa oficial, brasão PUC, margens e espaçamento do template. Título provisório recuperado do README principal, dois nomes documentados e composição a confirmar. |
| Fonte principal e bibliografia | `entrega-1.tex` e estilo `plainnat`. | `main.tex`, `referencias.bib` e estilo autor-data do `abntex2cite` com `\cite` e `\citeonline`. |
| Problema e revisão | Seções preenchidas em versão assistida. | Estrutura oficial com campos para redação pelo grupo. Conferir a revisão em 2 a 3 páginas após preenchimento. |
| Protocolo e matriz | Tabela de busca e matriz horizontal com oito trabalhos. | Apêndice A com campos de busca e critérios. Apêndice B no formato oficial, com dois blocos iniciais para copiar até ter um bloco por trabalho. |
| Nota de autoria | Autoria pendente. | Apêndice C com nota de autoria a completar. |
| Link somente leitura | Campo pendente. | Macro `\LINKPROJETO` no bloco **DADOS DO GRUPO**, com indicação visível até receber o link. |

## Do ZIP à entrega

1. No Overleaf, use **New Project → Upload Project** e selecione o ZIP. Em **Settings**, confirme `main.tex` como **Main document**.
2. O grupo confirma a composição, preenche as seções e a matriz com as obras que leu e selecionou, cadastra as entradas do `.bib` e registra a autoria no Apêndice C. A compilação inicial serve para conferir a estrutura. A bibliografia passa a exibir as obras conforme elas forem citadas.
3. Em **Share → Link sharing**, copie o link **Anyone with this link can view**. Cole o endereço de leitura dentro das chaves de `\newcommand{\LINKPROJETO}{}`, escreva cada `#` do endereço como `\#` e recompile. Teste o link clicável do PDF em uma janela anônima.
4. Após preencher todos os campos, remova a indicação de base editável da capa. Baixe o PDF e confira capa, extensão da revisão, apêndices, referências e citações resolvidas. Esse é o arquivo previsto pelo guia para envio.

Em 27/11/2026, o ZIP foi regenerado a partir da pasta editável. A prévia técnica foi compilada a partir do ZIP extraído. A cópia local do template e a minuta interna também foram recompiladas. A publicação no Overleaf e o teste anônimo do link real dependem do projeto do grupo.
