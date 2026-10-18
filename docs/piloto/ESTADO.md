# Estado do piloto do desfecho

Arquivo de passagem entre sessões. Cada sessão lê **só** este arquivo e o
`PROMPT-piloto-desfecho.md`, executa a próxima etapa pendente e atualiza esta tabela.

| Etapa | Situação | Saídas | Números principais |
|---|---|---|---|
| 1 — Modelos e marco zero | **Concluída (03/10/2026)** | `dados/intermediario/piloto_modelos.csv`; `piloto_fontes.csv` (17 brutos, 3,3 MB, em `dados/bruto/`) | 5 modelos; anúncio e dia 1 no Bedrock coincidem em todos |
| 2 — Eventos datados | **Concluída (03/10/2026)** | `src/coleta/piloto_eventos_datados.py`; `dados/intermediario/piloto_eventos_datados.csv` | 49 eventos (27 de disponibilidade); só 10 com região fora dos EUA para os 5 modelos |
| 3 — Snapshots do Wayback | **Concluída (03/10/2026)** | `src/coleta/piloto_wayback_bedrock.py`, `src/coleta/piloto_parser_bedrock.py`; `dados/intermediario/piloto_cdx.csv`, `piloto_presenca.csv` (13.222 linhas); 84 brutos `dados/bruto/wayback_*.html` (3,7 MB, gzip) | 173 dias de captura na janela, 84 conteúdos distintos, 0 falhas; troca de página em 21–22/04/2026 |
| 4 — Intervalos e precisão | **Concluída (03/10/2026)** | `src/tratamento/piloto_intervalos.py`; `dados/intermediario/piloto_eventos.csv`; `resultados/tabelas/piloto_precisao.md` | 145 pares, 86 eventos, 59 censurados, 0 truncados; **mediana da largura 14 dias** (P90 37); 13% com data exata; 10 conflitos |
| 5 — Veredito | **Concluída (03/10/2026)** | `docs/piloto/VEREDITO.md` | Passa no critério (14 d ≤ 30) sob a definição A; recomenda manter a pergunta regional, com 3 condições |

## Decisões tomadas antes da coleta

- Limiar de decisão: mediana da largura ≤ 30 dias (council de 03/10/2026).
- Tipo de disponibilidade usado no critério: `In-Region`, salvo escolha diferente do grupo
  registrada **aqui** antes da etapa 4.
- **Decisão do grupo em 03/10/2026, antes da etapa 4 e antes de ver qualquer intervalo:**
  **opção A.** "Disponível numa região" passa a ser **acessível a um cliente daquela
  região de qualquer forma** (In-Region, Geo ou Global; na página antiga, `Yes` ou `Yes*`).
  Células **"Legacy" contam como disponível.** Motivo: a página antiga só mede essa
  noção (achado 1 da etapa 3). Consequência registrada: a pergunta deixa de ser sobre
  infraestrutura local e passa a ser sobre acesso; a definição do §7.3 do escopo v1 e a
  Ficha precisam ser atualizadas.

## Onde parou

Etapa 1 concluída em 03/10/2026, na branch `piloto-desfecho`, sem commit.

Modelos escolhidos (anúncio = dia 1 no Bedrock):

| Modelo | Data | Período do Wayback |
|---|---|---|
| Claude 3.5 Sonnet | 2024-06-20 | ralo (pior caso) |
| Claude 3.5 Sonnet v2 | 2024-10-22 | ralo |
| Claude 3.7 Sonnet | 2025-02-24 | médio |
| Claude Sonnet 4.5 | 2025-09-29 | denso |
| Claude Sonnet 4.6 | 2026-02-17 | denso, atravessa a troca de página (2026-03-11) |

### Achados da etapa 1 que mudam as etapas seguintes

1. **O `doc-history` quase não registra expansão por região.** As entradas "Region
   expansion" de Claude são só GovCloud (3.7 Sonnet, 07/07/2025), batch (02/04/2025) e
   perfis entre regiões (06/11/2024). Na etapa 2, a fonte datada de expansão regional vai
   ser o What's New e o blog da AWS, não o doc-history. Exemplos já vistos: posts de
   inferência global para Tailândia/Malásia/Singapura/Indonésia/Taiwan e para Emirados/Bahrein.
2. **O `doc-history` tem datas erradas.** O legado do Claude Opus 4 aparece em
   01/10/2024, antes de o modelo existir; o Claude 3 Opus tem "New model" em 16/04 e
   07/06/2024; o Sonnet 4.5, em 25/09 e 29/09/2025. Toda data do doc-history precisa de
   uma segunda fonte.
3. **A partir de 2026 o doc-history não registra mais lançamentos de Claude** (último
   "New model": Opus 4.5, 24/11/2025). O Sonnet 4.6 foi datado pelo What's New.
4. **A página nova marca status nas células**, como "Legacy (EOL: 2026-07-30)", e modelos
   aposentados saem dela. O parser da etapa 3 deve tratar `Legacy` como presente, e
   ausência depois de EOL como saída, nunca como "nunca disponível".
5. **IDs a confirmar na etapa 3:** Claude 3.5 Sonnet (v1) e 3.7 Sonnet não aparecem nas
   páginas atuais. Os snapshots antigos trazem os IDs.
6. O marco zero na forma (b), primeira aparição em qualquer região, só sai na etapa 3.

Brutos já baixados que a etapa 2 deve **reaproveitar, sem baixar de novo**:
`dados/bruto/aws_bedrock_doc-history_2026-10-03.html`,
`aws_bedrock_models-region-compatibility_2026-10-03.html` (estado atual, que serve de
ponto final da série) e `aws_whatsnew_claude-sonnet-4-6_2026-10-03.html`.

### Etapa 2 (03/10/2026)

Fontes: What's New da AWS (API pública `aws.amazon.com/api/dirs/items/search`, diretórios
`whats-new` e `whats-new-v2`, tag Amazon Bedrock: 359 posts distintos desde 2024), blog da
AWS (mesma API, `blog-posts`, busca textual) e o doc-history baixado na etapa 1. O CSV
ganhou a coluna `natureza` (`disponibilidade` / `recurso`), para separar a chegada de um
modelo a uma região de anúncios de recurso (Knowledge Bases, prompt caching etc.).

Eventos de disponibilidade com região fora dos EUA, por modelo: 3.5 Sonnet 1 (07/08/2024:
Tóquio, Singapura, Frankfurt), 3.5 Sonnet v2 1 (10/02/2025: Sydney), 3.7 Sonnet 2 (Europa,
09/04 e 20/06/2025), Sonnet 4.5 4 (Japão/Austrália 31/10/2025, Canadá 24/11/2025, Oriente
Médio 24/02/2026, Nova Zelândia 26/03/2026), Sonnet 4.6 2 (Oriente Médio, Nova Zelândia).

### Achados da etapa 2 que mudam as etapas seguintes

1. **As fontes datadas cobrem uma fração pequena dos pares.** São cerca de 30 regiões fora
   dos EUA × 5 modelos, e os eventos datados nomeiam regiões para poucos deles. A data da
   maior parte dos pares vai sair dos intervalos do Wayback: **a etapa 3 decide o piloto.**
2. **Os posts de lançamento quase nunca listam regiões**: mandam "consultar a
   documentação". As listas de região estão nos posts de expansão posteriores.
3. **Os modelos recentes chegam via inferência entre regiões, não local.** O Sonnet 4.5
   estreou "via global cross region inference", e todos os eventos datados dele e do 4.6
   fora dos EUA são `geo` ou `global`. Se a definição do projeto ficar só em `In-Region`, as
   fontes datadas não dizem quase nada sobre os modelos de 2025–2026. **Essa escolha de
   definição é do grupo e precisa ser feita antes da etapa 4.**
4. Alguns posts do blog (África do Sul: "Claude 4.5 models"; Índia; Sudeste Asiático)
   não nomeiam modelos do piloto de forma inequívoca e ficaram como "sem modelo nomeado"
   ou de fora. Os snapshots resolvem.
5. Nos posts do blog, a região vem como país (`pais:Japan`). O mapeamento para códigos
   (Japão → ap-northeast-1/3?) deve ser feito na etapa 4, conferido contra os snapshots,
   e não adivinhado.

### Etapa 3 (03/10/2026)

- **Capturas na janela 02/05/2024–30/06/2026 (status 200):** página antiga, 117 dias (59
  conteúdos distintos); página nova, 56 dias (25 conteúdos). Como dias com o mesmo
  *digest* têm conteúdo idêntico, só 84 arquivos foram baixados. Os brutos vêm comprimidos
  em gzip, como o Wayback guardou; o parser descomprime na leitura e o bruto fica intacto.
- **Troca de página:** a página antiga é informativa até 20/04/2026; a partir de
  22/04/2026 é só o aviso "has moved" (11 dias `sem_info`). A nova começa em 11/03/2026, e
  as duas coexistem por 18 dias com dados nos dois lados.
- **Três layouts:** 2024 (uma tabela só com as regiões "fora das principais"; os EUA não
  aparecem, então a primeira aparição nos EUA em 2024 é artefato); 2025 (com coluna de
  provedor; `Yes`/`Yes*`/`No`); página nova (uma tabela por modelo, In-Region/Geo/Global,
  ícones e textos como "Legacy (EOL: …)").
- **Primeira aparição, de qualquer forma, fora dos EUA:** 3.5 Sonnet 29/08/2024;
  3.5 Sonnet v2 06/02/2025; 3.7 Sonnet 13/04/2025; Sonnet 4.5 30/09/2025 (um dia depois do
  anúncio, já em 29 regiões); Sonnet 4.6 02/03/2026 (13 dias depois do anúncio: buraco
  entre capturas). Regiões fora dos EUA alguma vez com acesso: 9, 7, 12, 29 e 29.

### Achados da etapa 3 que mudam as etapas seguintes

1. **A página antiga não mede In-Region.** Na sobreposição, 94% dos `Yes` da página
   antiga (1.023 de 1.088 pares-dia) são só Geo/Global na página nova. O asterisco
   (`Yes*`, "acessível só via inferência entre regiões") cobria só parte desses casos.
   O parser grava a página antiga como `qualquer` (acessível de alguma forma) e
   `so_cross_region`. **Consequência: historicamente só se mede "acessível de qualquer
   forma".** In-Region só tem série a partir de 11/03/2026, o que não cobre a chegada de
   nenhum dos 5 modelos. Se o grupo mantiver In-Region como definição, o piloto falha por
   construção.
2. **O Sonnet 4.5 não roda In-Region em nenhuma das 35 regiões** em 30/06/2026; o 4.6 tem
   In-Region em poucas. Os modelos novos chegam "fora dos EUA" no dia 1, mas via
   roteamento global.
3. **Divergência em sentido contrário:** 105 pares-dia em que a página antiga diz `No` e
   a nova diz In-Region são, na maioria, células "Legacy (EOL: …)" do 3.5/3.7 Sonnet. O
   parser conta "Legacy" como presente. A etapa 4 deve decidir se Legacy conta.
4. IDs do Claude 3.5 Sonnet (v1) e do 3.7 Sonnet seguem pendentes: as tabelas de região
   não trazem IDs. Não afeta o desfecho.

### Etapa 4 (03/10/2026)

Definição aplicada: opção A (acessível de qualquer forma, Legacy conta). 29 regiões fora
dos EUA × 5 modelos = 145 pares.

| Grupo | Eventos | Mediana largura | P90 largura | Censurados | Conflitos |
|---|---|---|---|---|---|
| Total | 86 | **14 d** | 37 d | 59 | 10 |
| Lançados em 2024 | 16 | 25 d | 119 d | 42 | 1 |
| Lançados em 2025 | 41 | 1 d | 26 d | 17 | 8 |
| Lançados em 2026 | 29 | 14 d | 14 d | 0 | 1 |

Achados para o veredito (etapa 5):

1. **Pelo critério registrado, o piloto passa:** mediana de 14 dias ≤ 30, nenhum par
   truncado. Os 59 censurados não são falta de dado: são pares que nunca receberam o
   modelo até 30/06/2026, que é o próprio desfecho censurado à direita.
2. **A precisão depende do período.** A coorte de 2024 tem mediana de 25 dias e P90 de 119
   (capturas ralas em 2024); a de 2025, mediana de 1 dia. A incerteza alta fica concentrada
   nos modelos de 2024.
3. **Os 10 conflitos são um problema de construto, não de precisão.** Em 8 deles, a página
   antiga mostra o Sonnet 4.5 acessível no Japão, na Austrália, no Canadá e no Bahrein desde o
   dia 1 (30/09/2025), mas o blog da AWS anuncia o acesso nesses países só depois (31/10/2025,
   24/11/2025, 24/02/2026). Duas leituras possíveis: (a) o blog anuncia um tipo diferente (Geo
   no país), enquanto o Global já existia; (b) o `Yes` da página antiga listava regiões que
   recebem tráfego do roteamento global, e não regiões de onde um cliente pode chamar o
   modelo. Se for (b), a definição A superestima o acesso dos modelos recentes. Os outros 2
   conflitos são a documentação adiantando-se ao anúncio em 4 a 9 dias.
4. A mediana da defasagem (ponto médio) é 6 dias no total, mas 77–119 dias para os modelos
   de 2024 e 0 para o Sonnet 4.5. Isso é resultado, não precisão, e só vale com a ressalva
   do item 3.

### Etapa 5 (03/10/2026)

Veredito em `docs/piloto/VEREDITO.md`. **O piloto terminou.** Recomendação: manter a
pergunta regional como principal (Bedrock como espinha dorsal), desde que (1) se feche o
construto do `Yes` antigo (região de origem ou de destino do roteamento global) com as
capturas de `inference-profiles-support.html` de out–nov/2025; (2) se usem métodos para
censura intervalar, com os modelos de 2024 também numa análise de sensibilidade; (3) se
repita a etapa 3 num modelo do Vertex antes de prometer as três plataformas. A decisão de
escopo da semana 8 é do grupo.
