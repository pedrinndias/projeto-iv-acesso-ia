# Prompt de execução: piloto do desfecho (Claude × AWS Bedrock)

> Prompt autocontido para sessões dedicadas, uma por etapa. Escrito em 03/10/2026.
> Ao abrir cada sessão: cole este arquivo **ou** peça "leia `docs/piloto/PROMPT-piloto-desfecho.md`
> e `docs/piloto/ESTADO.md` e execute a próxima etapa pendente".

---

## Por que este piloto existe

Projeto: *Desigualdade geográfica no acesso a modelos de IA generativa comercial*
(Projeto em Ciência de Dados IV, PUC Minas, dupla Pedro Dias Soares e Eduardo Velloso Landeiro).
O desfecho principal é a **defasagem em dias** entre a primeira disponibilidade de um modelo
e sua chegada a cada região de nuvem.

Em 03/10/2026, semana 7 de 16, esse desfecho ainda não existe: ninguém levantou a data de
lançamento nem a data de entrada por região de nenhum modelo. O council da mesma data
decidiu **não cortar nem manter o escopo às cegas**: primeiro provar, com 5 modelos, que o
desfecho pode ser medido com precisão útil. A decisão de escopo vai para a **semana 8**.

**Pergunta do piloto:** com fontes públicas, a data em que um modelo Claude chegou a uma
região do Bedrock pode ser determinada com incerteza mediana de até 30 dias?

---

## Modelo e esforço por etapa

Escolha no seletor do app **antes** de começar cada sessão. Uma etapa por sessão: cada
sessão começa lendo só este prompt e o `ESTADO.md`, e não relê o que a anterior já leu.

| Etapa | Trabalho | Modelo | Esforço | Teto de chamadas |
|---|---|---|---|---|
| 1 | Escolher os 5 modelos e levantar o marco zero | Sonnet 5.5 | médio | 20 |
| 2 | Extrair eventos datados das fontes oficiais da AWS | Sonnet 5.5 | médio | 20 |
| 3 | Baixar e interpretar os snapshots do Wayback | Sonnet 5.5 | **alto** (parser de vários layouts) | 35 |
| 4 | Montar os intervalos e medir a precisão | Sonnet 5.5 | médio | 15 |
| 5 | Aplicar o critério e redigir o veredito | Opus 5.5 | médio | 8 |
| — | Reexecutar um script pronto, conferir arquivos, `git status` | Haiku 4.5 | baixo | 5 |

Bateu o teto da etapa: **pare**, atualize o `ESTADO.md` com o ponto exato em que parou e
reporte. Não estoure o teto para "terminar rapidinho".

### Regras de economia de tokens (valem para todas as etapas)

1. **HTML nunca entra no contexto.** As páginas têm de 100 KB a 1,2 MB. Todo conteúdo
   baixado vai para disco e é lido **por script**. O script imprime no máximo 60 linhas
   (`| head -60`).
2. **Uma verificação = um script.** Nada de abrir arquivo para "dar uma olhada".
3. Snapshots do Wayback em versão crua: `https://web.archive.org/web/<timestamp>id_/<url>`.
   O sufixo `id_` devolve o HTML original, sem a barra do Wayback.
4. Para pesquisa na web, use WebSearch em modo `standard` e WebFetch com pergunta
   específica ("qual a data de publicação deste anúncio?"), nunca a página inteira.
5. Sem subagentes, hooks, cron ou tarefas agendadas.
6. Relatório de fim de etapa com no máximo 15 linhas.

---

## Fatos já verificados em 03/10/2026 (não reverificar)

| Fonte | Situação |
|---|---|
| `docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html` | **Esvaziada.** Hoje diz "Information previously on this page has moved". O Wayback tem 206 dias de snapshots, de 05/03/2024 a 25/08/2026, mas parte dos de 2026 deve ser só o aviso. **Achar a data da troca é tarefa da etapa 3** |
| `.../models-supported.html` | Também esvaziada, mesmo aviso |
| `.../models-region-compatibility.html` | **Página nova.** 1,2 MB, com uma tabela por modelo: Região × `In-Region` / `Geo` / `Global`. Wayback: 153 dias, de 11/03/2026 a 02/10/2026 |
| `.../doc-history.html` | Histórico **datado** da documentação: 118 KB, entradas de 28/09/2023 a 29/09/2026, 43 menções a Claude, com entradas do tipo "Region expansion". Exemplos: 06/11/2024 (perfis de inferência entre regiões para Claude), 04/04/2025 (batch), 15/07/2025 (Claude 3…) |
| `aws.amazon.com/about-aws/whats-new/recent/feed/` | RSS do What's New: responde, mas só traz itens recentes. Anúncios antigos exigem busca no site |
| `www.anthropic.com/news` | Responde: fonte do anúncio oficial de cada modelo |
| `src/coleta/cobertura_wayback.py` | Já trata as armadilhas da API CDX: exige HTTPS; sob limitação de taxa devolve HTML com status 200 (checar se o corpo começa com `[`); espera progressiva. **Reaproveite a função `consultar()`** |

---

## Definições operacionais do piloto

- **Três tipos de disponibilidade**, sempre registrados separadamente: `In-Region`
  (inferência sob demanda na própria região), `Geo` (roteamento entre regiões da mesma
  geografia) e `Global`. A definição do projeto (escopo v1, §7.3) conta como "disponível"
  apenas a inferência local, mas **o piloto registra os três**: a escolha final é do grupo
  e depende do que os dados mostrarem.
- **Marco zero**, também registrado de duas formas: (a) data do anúncio oficial do modelo;
  (b) primeira aparição do modelo em qualquer região do Bedrock. A Ficha define (b), e (a)
  serve de conferência.
- **Evento**: primeira vez que o par modelo × região aparece com um dado tipo de
  disponibilidade.
- **Intervalo do evento**: `(L, U]`, em que `U` é o primeiro snapshot com o par e `L` é o
  último snapshot **informativo** anterior sem ele. A data real está em algum ponto do
  intervalo, que **não é ruído simétrico** (é censura intervalar).
- **Snapshot informativo**: aquele em que o parser encontrou a tabela do modelo. Página
  reestruturada, aviso de "has moved" ou tabela ausente = `sem_info`, **nunca**
  "indisponível".
- **Truncado à esquerda**: o par já aparece no primeiro snapshot informativo, sem
  início conhecido.
- **Censurado à direita**: o par nunca aparece até o último snapshot informativo.
- **Data exata**: quando uma fonte datada (doc-history, What's New, anúncio) cai dentro de
  `(L, U]`, a data é exata e a largura vira 0. Se cair fora do intervalo, registrar como
  `conflito`, sem descartar.

---

## Etapas

### Etapa 1 — Os 5 modelos e o marco zero

Começo: `git status`; criar a branch `piloto-desfecho` a partir da `main` (nunca com prefixo
`claude/`); criar o `docs/piloto/ESTADO.md` se não existir.

Escolha dos 5 modelos Claude: espalhados pelos períodos de densidade do Wayback, para que o
teste inclua o pior caso.

| Período | Densidade de snapshots | Candidatos (datas a confirmar na fonte primária) |
|---|---|---|
| 2024 | rala (1 dia no 3º trimestre) | Claude 3.5 Sonnet (jun/2024); Claude 3.5 Sonnet v2 (out/2024) |
| 2025 | média a densa | Claude 3.7 Sonnet (fev/2025); Claude Sonnet 4.5 (set/2025) |
| 2026 | densa, mas com a troca de página | um modelo lançado perto de **março/2026**, para testar a emenda entre a página antiga e a nova. Escolher pelo `doc-history` |

Saída: `dados/intermediario/piloto_modelos.csv`, com as colunas
`modelo, id_bedrock, data_anuncio, url_anuncio, data_bedrock_dia1, url_bedrock_dia1, observacoes`.
Toda data tem URL. Data sem fonte fica vazia, e não estimada.

**Parar e reportar.**

### Etapa 2 — Eventos datados das fontes oficiais

Script: `src/coleta/piloto_eventos_datados.py`. Ele baixa o `doc-history.html`, salva em
`dados/bruto/` e extrai as entradas que citam os 5 modelos ou "Region expansion" de Claude.
Para cada modelo, procurar também os anúncios do What's New sobre expansão de região
(busca no site; anotar a URL de cada um).

Saída: `dados/intermediario/piloto_eventos_datados.csv`, com as colunas
`data, modelo, regioes, tipo, url, trecho` (trecho com no máximo 200 caracteres, para
auditoria).

**Parar e reportar** quantos eventos datados existem por modelo.

### Etapa 3 — Snapshots do Wayback (a etapa cara)

Script: `src/coleta/piloto_wayback_bedrock.py`.

1. Listar via CDX os snapshots das duas páginas (`models-regions.html` e
   `models-region-compatibility.html`), um por dia.
2. Baixar só os snapshots da janela dos 5 modelos: do marco zero de cada um até o último
   snapshot disponível. Espera de 3 a 5 s entre requisições.
3. Salvar **sem subpasta**, como `dados/bruto/wayback_<pagina>_<timestamp>.html`. O
   `.gitignore` só cobre `dados/bruto/*.html`; uma subpasta seria commitada.
4. **Aprender os layouts antes de escrever o parser.** Em 3 snapshots (um de 2024, um de
   2025 e um da página nova), o script imprime só os cabeçalhos das tabelas e as 5
   primeiras linhas, truncadas. Os layouts mudaram ao longo do tempo.
5. **Achar a data da troca:** o primeiro snapshot da página antiga que é só o aviso.
6. O parser grava `dados/intermediario/piloto_presenca.csv`, com as colunas
   `pagina, timestamp, modelo, regiao, tipo, situacao` (`situacao` ∈ `presente`,
   `ausente`, `sem_info`). No layout antigo, se não for possível distinguir os tipos,
   `tipo = indistinto`.
7. Proveniência: `dados/intermediario/piloto_fontes.csv`, com as colunas
   `url, timestamp, arquivo, sha256, data_coleta, script`. O arquivo `.meta.json` não
   serve: o `.gitignore` atual o ignora.

**Parar e reportar:** snapshots baixados, quantos são `sem_info`, a data da troca de
página e se os 5 modelos foram encontrados.

### Etapa 4 — Intervalos e precisão

Script: `src/tratamento/piloto_intervalos.py`. Ele combina presença e eventos datados e
grava `dados/intermediario/piloto_eventos.csv`, com as colunas
`modelo, regiao, tipo, L, U, largura_dias, data_exata, origem, truncado_esquerda, censurado, conflito`.

Resumo em `resultados/tabelas/piloto_precisao.md`, por tipo de disponibilidade, só para
regiões fora dos EUA:

- nº de eventos; % com data exata; mediana e percentil 90 da largura em dias;
- nº de pares truncados à esquerda e censurados; nº de conflitos;
- a mesma tabela separada por período (2024, 2025, 2026).

**Parar e reportar.**

### Etapa 5 — Veredito (Opus 5.5)

Ler **só** `resultados/tabelas/piloto_precisao.md` e o `ESTADO.md`. Aplicar o critério
abaixo e escrever o `docs/piloto/VEREDITO.md` (no máximo 1 página): resultado, critério
aplicado, ressalvas e o que muda na Ficha. **A decisão de escopo é do grupo**; o veredito
recomenda.

---

## Critério de decisão (registrado antes de ver os dados)

Aplicado ao tipo de disponibilidade que o grupo escolher como definição. Na falta de
escolha, `In-Region`.

- **Mediana da largura ≤ 30 dias** → a pergunta regional segue. Na análise, usar métodos
  de censura intervalar e sensibilidade aos truncados à esquerda.
- **Mediana > 30 dias, ou mais da metade dos pares truncados ou `sem_info`** → a pergunta
  co-primária (países) vira a principal na semana 8, e a regional vira descritiva.

O limiar de 30 dias veio do council de 03/10/2026. **Se o grupo quiser mudar, mude agora,
antes da etapa 4.** Mudar depois de ver o número é viés de confirmação.

---

## Regras do repositório

- `dados/bruto/` é imutável; correções vão para `dados/intermediario/` via script.
- Todo dado guarda URL de origem e data da coleta.
- Scripts só com biblioteca padrão do Python, como os existentes.
- Commits só com o nome do Pedro: sem `Co-Authored-By`, sem "Generated with". Commitar
  apenas quando o Pedro pedir. A `main` fica entregável; o trabalho vai na branch
  `piloto-desfecho`.
- Ao fim de cada etapa, atualizar o `docs/piloto/ESTADO.md`: etapa concluída, arquivos
  gerados, números principais e próximo passo.
