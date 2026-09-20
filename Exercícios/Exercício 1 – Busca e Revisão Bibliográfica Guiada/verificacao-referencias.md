# Verificação de existência das referências

Conferência feita em **11 de setembro de 2026**, contra as APIs da Crossref
(`api.crossref.org/works/{doi}`), da DataCite (`api.datacite.org/dois/{doi}`) e do
arXiv (`export.arxiv.org/api/query`). Nenhuma referência entrou em `referencias.bib`
sem que autoria, ano, título e veículo tivessem sido conferidos contra o registro
da fonte.

## Trabalhos selecionados (entram na tabela comparativa)

| # | Referência curta | DOI / identificador | Registro | Conferido |
|---|---|---|---|---|
| 1 | Lutz (2019) | `10.1002/hbe2.140` | Crossref | Título, autoria (1), ano e veículo (*Human Behavior and Emerging Technologies*) batem |
| 2 | Amos et al. (2021) | `10.1145/3442381.3450048` | Crossref | `proceedings-article`, *Proceedings of the Web Conference 2021* |
| 3 | Knez (2023) | `10.1007/s00191-023-00830-w` | Crossref | *Journal of Evolutionary Economics* |
| 4 | Mannuru et al. (2023) | `10.1177/02666669231200628` | Crossref | *Information Development* |
| 5 | Wang et al. (2024) | `10.1177/14614448241232345` | Crossref | *New Media & Society* |
| 6 | McElheran et al. (2024) | `10.1111/jems.12576` | Crossref | *Journal of Economics & Management Strategy* |
| 7 | Mügge (2024) | `10.1080/13501763.2024.2318475` | Crossref | *Journal of European Public Policy* |
| 8 | Furtado e Evangelista (2024) | `10.18617/liinc.v20i2.7272` | Crossref | *Liinc em Revista*, v. 20, n. 2, 28/11/2024, acesso aberto |
| 9 | Ahmed e Wahed (2020) | `10.48550/arXiv.2010.15581` | DataCite + arXiv API | `Preprint`, cs.CY, submetido em 22/10/2020, 2 autores; landing page HTTP 200 |
| 10 | Sastry et al. (2024) | `10.48550/arXiv.2402.08797` | DataCite + arXiv API | `Preprint`, cs.CY, submetido em 13/02/2024, 19 autores; landing page HTTP 200 |

## Referências de contexto (citadas no texto, fora da tabela)

| Referência curta | DOI | Registro | Conferido |
|---|---|---|---|
| van Deursen e van Dijk (2018) | `10.1177/1461444818797082` | Crossref | *New Media & Society* |
| Santos, Pimenta e Nobre (2007) | `10.1590/S0104-11692007000300023` | Crossref | *Revista Latino-Americana de Enfermagem* |

## Ocorrências registradas durante a verificação

1. **Os dois preprints do arXiv retornaram HTTP 404 na Crossref.** Não é ausência de
   registro: DOIs com prefixo `10.48550` são registrados na **DataCite**, não na
   Crossref. Ambos foram confirmados na DataCite e, de forma independente, na API do
   próprio arXiv, com conferência de autoria, data de submissão e categoria.

2. **Nenhum trabalho foi descartado por falha de verificação.** Dois trabalhos
   recuperados pelas buscas foram descartados por critério temático, não por dúvida
   sobre sua existência: Besiroglu et al. (2024), por sobreposição com Ahmed e Wahed
   (2020), e Prates e Chiarini (2024), mantido como reserva.

3. **Sastry et al. (2024) tem 19 autores.** Sob ABNT, a entrada usa o primeiro autor
   seguido de *et al.*; o campo `author` do `.bib` traz a lista completa para que o
   `biblatex` faça o corte.

## Pendência antes da entrega

A análise registrada na tabela comparativa foi construída a partir dos **resumos e
metadados** obtidos nas APIs, e não da leitura integral dos dez textos. Isso está
declarado no corpo do trabalho, na seção 3, e assinalado na coluna de limitações.
**A leitura integral precisa ser feita antes da entrega**, com atenção especial às
colunas *Principais resultados* e *Limitações observadas*, que são as mais sensíveis
a essa diferença. Todos os dez trabalhos são de acesso aberto ou têm versão acessível
pelo DOI.
