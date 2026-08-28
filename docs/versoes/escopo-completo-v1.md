# Projeto em Ciência de Dados IV — Ficha Inicial e Escopo do Projeto
### Versão 1 · PUC Minas · 2º semestre de 2026 · Prof. Rodrigo Richard Gomes

> **Base normativa deste documento:** slides *PCDIV — Aula 01, "Da curiosidade à pergunta investigável"*.
> **Base metodológica da problematização:** SANTOS, C. M. C.; PIMENTA, C. A. M.; NOBRE, M. R. C. *A estratégia PICO para a construção da pergunta de pesquisa e busca de evidências*. Rev. Latino-Am. Enfermagem, v. 15, n. 3, maio–jun. 2007.

---

## 0. Sumário executivo — leia isto primeiro

O tema trazido pelo grupo foi:

> *"Por que as empresas de IA americanas (como a Anthropic) limitam o processamento dos seus agentes para empresas de fora dos EUA."*

**Esse enunciado, como está, não é uma pergunta de pesquisa investigável — é um problema mal-formulado com uma conclusão embutida.** A Seção 2 detalha os três defeitos. A boa notícia: o tema é excelente, é original, é relevante e **os dados existem** — o que precisa mudar é a *forma* da pergunta, não o assunto.

A reformulação proposta troca **"por que limitam"** (pergunta sobre intenção corporativa, respondível apenas com documentos internos que não temos) por **"existe, de quanto é, e o que explica"** (pergunta sobre um fenômeno mensurável, respondível com dados públicos). O "porquê" não é abandonado: ele retorna como **hipóteses concorrentes testáveis** (infraestrutura, mercado, regulação, geopolítica), que viram variáveis explicativas.

**Pergunta de pesquisa resultante:**

> **Quais fatores estão associados à defasagem de disponibilidade regional de modelos de IA generativa comercial de provedores estadunidenses (Anthropic, OpenAI, Google) nas três principais plataformas de nuvem, entre abril de 2024 e junho de 2026?**

Esse movimento — de um "por quê" indignado para uma pergunta mensurável — **é literalmente o que o artigo do PICO ensina**, e está exemplificado nele (ver Seção 4.1). Não é uma concessão: é o método.

> ⚠️ **A janela começa em abril de 2024, e não em janeiro de 2023, por uma razão empírica, não arbitrária.** Antes de fechar este documento, testamos a disponibilidade real das fontes históricas (§ 7.5). Não existe dado recuperável de disponibilidade regional para 2023 — as páginas de documentação que registram essa informação só passaram a ser arquivadas em março/abril de 2024. Um recorte temporal deve ser justificado pelo dado que existe, não pelo dado que gostaríamos que existisse.

> ✅ **Exceção:** o desfecho de *atendimento por país* tem série desde **maio de 2023** (274 dias de snapshot). Por isso ele foi **promovido a desfecho co-primário** — ver § 5.5 e § 7.5.

---

## 1. Checklist das demandas ✅

### 1.1 Entregável formal da próxima aula — *Ficha Inicial do Projeto, Versão 1* (slide 19)

| # | Demanda | Status | Onde está |
|---|---|---|---|
| 1 | Área de interesse | ✅ | § 5.1 |
| 2 | Tema inicial | ✅ | § 5.2 |
| 3 | Problema de pesquisa | ✅ | § 5.3 |
| 4 | Justificativa | ✅ | § 5.4 |
| 5 | Pergunta de pesquisa | ✅ | § 5.5 |
| 6 | Que dados seriam necessários | ✅ | § 5.6 e § 7.2 |
| 7 | Onde esses dados poderiam estar | ✅ | § 5.7 e § 7.1 |

### 1.2 Critérios de uma boa pergunta de pesquisa (slide 16)

| Critério | Atende? | Evidência |
|---|---|---|
| **Clara** — qualquer um entende o que se quer saber | ✅ | Pergunta em § 5.5; termos definidos em § 7.3 |
| **Delimitada** — recorte de população, lugar e tempo | ✅ | População: pares modelo×região; Lugar: regiões de nuvem comerciais dos 3 provedores; Tempo: abr/2024–jun/2026, **recorte definido pela cobertura real das fontes, medida em § 7.5** |
| **Investigável** — respondível com dados | ✅ | Desfecho é numérico e observável; § 7 |
| **Viável** — cabe em um semestre | ✅ | Fontes **testadas empiricamente**, não apenas listadas — § 7.5. Cronograma em § 11 |
| **Relevante** — alguém se importa com a resposta | ✅ | § 5.4 (justificativa) |
| **Ética** — não expõe nem prejudica ninguém | ✅ | § 10. Dado institucional público, zero dado pessoal |
| **Teste de viabilidade** — "sabem apontar onde estão os dados?" | ✅ | 14 fontes nomeadas com URL e método (§ 7.1) **e cobertura histórica medida fonte a fonte** (§ 7.5) |

### 1.3 Regras da disciplina

| Regra | Cumprida? | Como |
|---|---|---|
| "A técnica serve à pergunta — nunca o contrário" (slide 5) | ✅ | Nenhuma técnica foi escolhida antes da pergunta. A análise de sobrevivência aparece em § 8.3 **derivada** do formato do desfecho (tempo-até-evento com censura à direita) — não por escolha estética |
| Não começar por "vamos usar rede neural / dashboard / treinar modelo" | ✅ | Nada disso está no projeto |
| Distinguir tema ≠ problema ≠ pergunta (slide 6) | ✅ | § 5.2, § 5.3 e § 5.5 são explicitamente os três níveis distintos |
| Cartão individual, sem nome de técnica (slide 17) | ✅ | § 12 — três versões, uma por integrante |

### 1.4 Etapas do projeto ao longo do semestre (slide 4)

| Etapa | Situação | Seção |
|---|---|---|
| tema | ✅ definido | § 5.2 |
| problema | ✅ definido | § 5.3 |
| pergunta | ✅ definida | § 5.5 |
| objetivos | ✅ antecipado | § 6 |
| revisão | ✅ antecipado (strings de busca prontas) | § 7.4 |
| metodologia | ✅ antecipado | § 8 |
| dados | ✅ antecipado | § 7 |
| análise | ✅ antecipado | § 8.3 |
| resultados | 🔜 depende da execução | § 9 (formato previsto) |
| apresentação | 🔜 depende da execução | § 11 |

> **Nota:** o slide 20 é explícito — hoje só as três primeiras etapas precisam existir. As demais estão aqui **como escopo antecipado**, porque o pedido foi construir o escopo completo. Elas serão refinadas nas próximas aulas e devem mudar.

### 1.5 Pendências que dependem do grupo, não deste documento

| Item | Status |
|---|---|
| Nomes e matrículas dos 3 integrantes | ⬜ preencher em § 5.0 |
| Preenchimento do formulário de registro do grupo (slide 18) | ⬜ um integrante, até o fim da aula |
| Escolha entre a pergunta principal (§ 5.5) e as alternativas (§ 3) | ⬜ decisão do grupo |
| Verificação dos itens marcados ⚠️ em § 13 | ⬜ antes da entrega |

---

## 2. Diagnóstico crítico do tema original

O enunciado original tem três defeitos, e vale entendê-los porque são os erros mais comuns em projeto de pesquisa — o slide 6 diz que "a maior parte dos projetos ruins para no primeiro nível".

### Defeito 1 — Pressupõe o fenômeno em vez de medi-lo

"Por que as empresas limitam..." afirma, sem ter verificado, que a limitação existe. Isso inverte a ordem da investigação: a pesquisa deixa de perguntar *se* e passa a procurar justificativa para uma conclusão já tomada. É viés de confirmação institucionalizado no desenho do estudo.

Um bom projeto tem que poder **refutar a própria hipótese do grupo**. Se a análise mostrar que a defasagem regional se explica inteiramente pela idade e capacidade da região de nuvem — e não por origem geopolítica —, esse é um resultado legítimo, publicável e mais interessante do que a confirmação. O desenho da Seção 8 permite exatamente isso.

### Defeito 2 — "Por quê" sobre intenção corporativa não é respondível com dados públicos

Responder *por que uma empresa decide* algo exige acesso a deliberação interna: atas, e-mails, entrevistas com quem decidiu. Isso não está disponível para um grupo de graduação em um semestre. Perguntas de intenção só são investigáveis com método qualitativo e acesso — que não temos.

O que **é** investigável é o comportamento observável da empresa e sua associação com fatores externos mensuráveis. Daí se **infere** o porquê, com as devidas ressalvas.

### Defeito 3 — "Limitam o processamento" é ambíguo: são pelo menos seis coisas diferentes

Sem escolher uma, não existe variável de desfecho. As leituras possíveis:

| Leitura | Mensurável? | Fonte existe? |
|---|---|---|
| (a) O país simplesmente não é atendido | Sim, binário | Sim — listas oficiais de países suportados |
| (b) O modelo mais novo demora a chegar na região | Sim, em dias | Sim — documentação datada |
| (c) Limites de taxa/quota menores fora dos EUA | Parcialmente | Documentação pública é incompleta |
| (d) Latência maior fora dos EUA | Sim, em ms | Requer medição própria |
| (e) Preço maior na mesma moeda | Sim, em US$/token | Sim — páginas de preço por região |
| (f) Recursos ausentes (batch, cache, janela de contexto) | Sim, binário por recurso | Sim — documentação |

**Este projeto adota (b) como desfecho primário** — é o mais bem documentado, o mais comparável entre provedores e o que tem série histórica recuperável. As leituras (a), (e) e (f) entram como **desfechos secundários**. A leitura (d), que é a mais literalmente próxima do que o grupo escreveu, entra como **extensão opcional** (§ 3, item B3) por depender de coleta ativa.

### O que se ganha com a reformulação

O "por quê" não some — ele vira quatro hipóteses concorrentes, cada uma com uma predição diferente e falseável (§ 8.2). O grupo continua respondendo a pergunta que o motivou, mas com evidência em vez de suposição.

---

## 3. Brainstorm — dez ângulos considerados e a triagem

Todas as ideias foram avaliadas contra os seis critérios do slide 16. A coluna decisiva, quase sempre, é *viável*.

| # | Ângulo | Desfecho mensurável | Viabilidade | Decisão |
|---|---|---|---|---|
| **B1** | **Defasagem de disponibilidade de modelos por região de nuvem** | Dias entre 1ª disponibilidade global e disponibilidade na região | **Alta** — documentação pública, parte com histórico Git | ✅ **ESCOLHIDO — desfecho primário** |
| B2 | Diferencial de preço do mesmo modelo entre regiões | US$ por milhão de tokens, por região | Alta | ✅ Incorporado como desfecho secundário |
| B3 | Latência real medida de vários países | ms (p50/p95) por ponto de vantagem | Média — exige VMs em ~6–8 países | ⚠️ Extensão opcional (§ 8.5) |
| B4 | Viés linguístico: desempenho em português vs. inglês | Escore em benchmark bilíngue | Média-alta | ❌ Muda o tema (vira "viés de modelo", não "acesso") — **guardar como projeto futuro** |
| **B5** | **Quais países ficam de fora da lista de atendimento** | Binário atendido/não atendido por país | **Alta** | ✅ Incorporado como desfecho secundário |
| B6 | Confiabilidade: incidentes e degradação por região | Nº e duração de incidentes | Baixa-média — status pages raramente desagregam por região | ❌ Descartado: dado insuficiente |
| **B7** | **Recursos disponíveis por região** (batch, cache, tool use, janela de contexto) | Nº de recursos disponíveis / total | **Alta** | ✅ Incorporado como desfecho secundário |
| B8 | Cláusulas contratuais dos Termos de Serviço por jurisdição | Análise documental | Média | ❌ Método documental-jurídico, não ciência de dados |
| B9 | Discurso público das empresas sobre soberania de IA | Análise de conteúdo | Média | ❌ Fora do escopo da disciplina |
| B10 | Difusão de data centers de IA anunciados por país | US$ investidos, MW instalados | Média — dados de imprensa, pouco padronizados | ⚠️ Fonte auxiliar para variável explicativa |

**Resultado da triagem:** B1 é o eixo, com B2, B5 e B7 como desfechos secundários que enriquecem sem inflar o escopo — todos vêm das mesmas páginas já raspadas para B1. B3 fica como extensão se sobrar tempo. B4 é uma boa ideia que o grupo deveria anotar para outro momento: é um projeto inteiro, não um adendo.

---

## 4. Problematização pela estratégia PICO

### 4.1 Por que o PICO se aplica aqui — e por que ele justifica a reformulação

O artigo de Santos, Pimenta e Nobre (2007) descreve o PICO como acrônimo de **P**aciente/Problema, **I**ntervenção, **C**omparação e **O**utcome (desfecho), e afirma que a estratégia "pode ser utilizada para construir questões de pesquisa de naturezas diversas" — não apenas clínicas.

**O ponto central para este projeto está no exemplo do próprio artigo.** Os autores relatam a revisão de Bergin e Wraight sobre curativos com prata: a ideia de pesquisa nasceu, nas palavras do artigo, *"com o questionamento do porquê da não utilização de curativos/agentes tópicos com prata"* — e a pergunta que efetivamente foi construída com o PICO foi **"qual o efeito de curativos/agentes tópicos contendo prata em sua composição no tratamento de úlceras de pé em diabéticos?"**.

Ou seja: **o artigo-referência da disciplina faz exatamente a conversão que estamos propondo** — parte de um "por que não fazem X?" e chega a uma pergunta sobre efeito mensurável. Nosso caso é isomorfo:

| | Bergin & Wraight (via Santos et al.) | Este projeto |
|---|---|---|
| Curiosidade inicial | Por que não usam curativos com prata? | Por que limitam o processamento fora dos EUA? |
| Pergunta construída com PICO | Qual o **efeito** de curativos com prata na cicatrização? | Quais **fatores** se associam à defasagem de disponibilidade regional? |

### 4.2 Adaptação: de PICO para PICOC

O PICO nasceu na saúde, onde "I" é uma intervenção que o pesquisador administra. Em estudo observacional não há intervenção — há **exposição**. Duas adaptações consagradas cobrem isso, e ambas são aplicadas aqui:

- **PECO** — troca *Intervention* por *Exposure*, padrão em epidemiologia observacional.
- **PICOC** — acrescenta *Context*, adaptação padrão em revisões sistemáticas da Computação (metodologia Kitchenham para Engenharia de Software).

Usar as duas adaptações não é licença poética: é a aplicação correta de um instrumento fora de seu domínio de origem, e deve ser **declarada explicitamente na metodologia** — o professor vai perguntar.

### 4.3 A tabela PICOC deste projeto

| Componente | Definição (Santos et al., 2007) | Neste projeto |
|---|---|---|
| **P** — População / Problema | Paciente único, grupo de pacientes ou problema de saúde | **Unidade de análise: o par (modelo de IA × região de nuvem).** Modelos de linguagem de propósito geral, de acesso comercial via API, dos provedores Anthropic, OpenAI e Google. Unidade secundária: o par (provedor × país) para os desfechos de atendimento e preço |
| **E/I** — Exposição (subst. Intervenção) | Intervenção de interesse | **Estar fora dos Estados Unidos**, operacionalizado em três variáveis não colineares: (i) bloco geoeconômico da região; (ii) regime regulatório de dados vigente (GDPR/AI Act, LGPD, outros); (iii) situação frente a controles de exportação e sanções dos EUA |
| **C** — Comparação | Intervenção padrão, ou nenhuma | **Regiões de nuvem sediadas nos Estados Unidos** (`us-east-1`, `us-east5`, `East US` e equivalentes), que funcionam como linha de base de disponibilidade — é nelas que os modelos costumam estrear |
| **O** — Outcome / Desfecho | Resultado esperado | **Primário:** defasagem, em dias, entre a primeira disponibilidade documentada do modelo em qualquer região e sua disponibilidade naquela região (com censura à direita para regiões que nunca receberam). **Secundários:** taxa de cobertura de modelos por região; atendimento ao país (binário); preço por milhão de tokens; nº de recursos habilitados |
| **C** — Contexto *(extensão PICOC)* | — | Plataformas AWS Bedrock, Google Vertex AI e Microsoft Foundry, além do acesso direto pelas APIs dos provedores. **Janela de abril/2024 a junho/2026** para o desfecho de disponibilidade regional e **de maio/2023 a junho/2026** para o desfecho de atendimento por país — limites determinados pela cobertura real das fontes, medida em § 7.5 |

### 4.4 Montagem mecânica da pergunta a partir do PICOC

Seguindo o procedimento do artigo, os componentes se encadeiam:

> **Entre modelos de IA generativa comercial de provedores estadunidenses disponibilizados nas principais plataformas de nuvem [P + Contexto], quais fatores associados à localização geográfica, ao regime regulatório e ao alinhamento geopolítico da região [E] estão relacionados a uma maior defasagem de disponibilidade [O] em comparação com as regiões sediadas nos Estados Unidos [C], no período de abril de 2024 a junho de 2026 [Contexto]?**

A versão enxuta, para a Ficha, está em § 5.5.

---

## 5. FICHA INICIAL DO PROJETO — VERSÃO 1

### 5.0 Identificação

| Campo | Preencher |
|---|---|
| Integrante 1 | ⬜ Nome / Matrícula |
| Integrante 2 | ⬜ Nome / Matrícula |
| Integrante 3 | ⬜ Nome / Matrícula |
| Disciplina | Projeto em Ciência de Dados IV |
| Semestre | 2º/2026 |

---

### 5.1 Área de interesse

Ciência de dados aplicada a **políticas de tecnologia e desigualdade digital**, na interseção entre economia da computação em nuvem, difusão de tecnologia e geopolítica da inteligência artificial.

---

### 5.2 Tema inicial

**Desigualdade geográfica no acesso a modelos de inteligência artificial generativa comercial.**

> *É um tema — amplo, sem recorte, não investigável como está. É o primeiro quadrado do slide 4, e está correto que seja assim.*

---

### 5.3 Problema de pesquisa

Modelos de IA generativa deixaram de ser curiosidade técnica e passaram a ser insumo produtivo: empresas, hospitais, universidades e órgãos públicos constroem sistemas em cima deles. Esse insumo, porém, é ofertado por um punhado de empresas concentradas em um único país, e **não chega a todos os lugares ao mesmo tempo, pelo mesmo preço, nem com os mesmos recursos**.

Existe percepção difundida — entre desenvolvedores e empresas fora dos Estados Unidos — de que o acesso a esses modelos é sistematicamente pior fora do território americano: chega depois, custa mais, oferece menos recursos, e às vezes não chega. **Essa percepção, no entanto, não está quantificada.** Não se sabe o tamanho real da defasagem, se ela é uniforme entre regiões, se vem diminuindo ou aumentando, nem — o ponto decisivo — **se ela se explica por fatores técnicos neutros** (uma região de nuvem nova simplesmente ainda não tem capacidade instalada, e recebe *todos* os serviços com atraso) **ou por fatores econômicos, regulatórios e geopolíticos** que operariam especificamente sobre IA.

Enquanto essa distinção não for feita com dados, a discussão pública sobre soberania digital e dependência tecnológica se apoia em anedota. Empresas brasileiras que precisam decidir onde hospedar sistemas críticos de IA decidem no escuro.

> *É um problema — diz o que incomoda, e por quê. Ainda não é uma pergunta.*

---

### 5.4 Justificativa

**Relevância prática.** A adoção de IA generativa no Brasil cresce, e a decisão de arquitetura — usar uma região local com menos modelos disponíveis, ou uma região americana com melhor oferta mas com implicações de residência de dados sob a LGPD — é hoje tomada sem métrica. Quantificar a defasagem transforma essa decisão em cálculo.

**Relevância para política pública.** O debate sobre soberania de IA, data centers nacionais e regulação de IA no Brasil se beneficia de evidência sobre a magnitude real da assimetria de acesso. Medir é pré-requisito para decidir se há algo a corrigir.

**Relevância científica.** Existe literatura consolidada sobre difusão de tecnologia e sobre divisão digital em termos de infraestrutura e conectividade. Há muito menos trabalho medindo **assimetria de acesso à camada de computação de IA** — que é uma forma nova de divisão digital, operando não sobre quem tem internet, mas sobre quem tem acesso à fronteira da capacidade computacional. O projeto se posiciona nessa lacuna.

**Relevância formativa.** O desenho exige justamente o que a disciplina quer treinar: construir uma base de dados que não existe pronta, definir o desfecho, identificar e controlar variáveis de confusão, e resistir à tentação de confirmar a hipótese de partida.

**Honestidade quanto ao risco.** É possível que o resultado contrarie a intuição do grupo — que a defasagem seja explicada por maturidade de região e desapareça o efeito geopolítico. Esse resultado seria igualmente válido e o projeto está desenhado para aceitá-lo.

---

### 5.5 Pergunta de pesquisa

> ### **Quais fatores estão associados à defasagem de disponibilidade regional de modelos de IA generativa comercial de provedores estadunidenses (Anthropic, OpenAI e Google), nas plataformas AWS Bedrock, Google Vertex AI e Microsoft Foundry, entre abril de 2024 e junho de 2026?**

**Pergunta co-primária** — promovida a este status por ter a melhor série histórica de todas as fontes testadas (§ 7.5):

> ### **Quais características dos países estão associadas à sua ausência das listas oficiais de atendimento dos provedores de IA estadunidenses, e como essa composição mudou entre maio de 2023 e junho de 2026?**

**Perguntas secundárias:**

1. Qual a magnitude da defasagem mediana de disponibilidade entre regiões dos EUA e regiões fora dos EUA, e como ela evoluiu no período?
2. Existe diferença de preço, para o mesmo modelo e mesmo volume, entre regiões dentro e fora dos EUA?
3. Em que posição o Brasil se situa no ordenamento de defasagem, e essa posição é compatível com seu porte econômico?
4. A defasagem de IA é maior do que a defasagem dos demais serviços de nuvem na mesma região — isto é, existe um atraso **específico de IA** além do atraso geral de infraestrutura?

**Verificação contra o slide 16:** clara (§ 1.2), delimitada em população/lugar/tempo, investigável (desfecho numérico observável), viável (fontes verificadas em § 7.1), relevante (§ 5.4), ética (§ 10).

---

### 5.6 Que dados seriam necessários

**Bloco A — Disponibilidade (constrói o desfecho)**

- Matriz **modelo × região × plataforma**, indicando disponibilidade em cada data.
- Data da **primeira disponibilidade global** de cada modelo (marco zero da defasagem).
- Data de **entrada de cada modelo em cada região** — é o dado mais difícil e o mais importante.
- Lista de **países atendidos** por cada provedor, com histórico de alterações.
- **Recursos** habilitados por modelo e região (batch, cache de prompt, uso de ferramentas, janela de contexto).

**Bloco B — Preço**
- Preço por milhão de tokens de entrada e de saída, por modelo, região e data.

**Bloco C — Variáveis de controle da região *(bloco decisivo)***
- **Data de lançamento da região de nuvem** e **número de zonas de disponibilidade**.
- **Número total de serviços da plataforma disponíveis naquela região** — proxy direto de maturidade da região.

> ⚠️ **Este é o dado mais importante de todo o projeto.** Sem ele, qualquer associação encontrada é ininterpretável. Se um modelo demora a chegar a São Paulo, mas *todo serviço da AWS* demora a chegar a São Paulo, o atraso é maturidade de região — não tratamento diferenciado à IA. É exatamente esse controle que separa uma pesquisa de uma denúncia.

**Bloco D — Variáveis explicativas do país/região**
- PIB, PIB per capita, população, grupo de renda.
- Indicadores de desenvolvimento de TIC e penetração de internet.
- Regime regulatório de proteção de dados vigente (GDPR/AI Act, LGPD, ausência de lei geral).
- Situação frente a controles de exportação e sanções dos EUA, com as datas de mudança de política.
- Presença de acordos de adequação de transferência internacional de dados com EUA/UE.

**Bloco E — Extensão opcional**
- Latência medida (p50, p95) a partir de pontos de vantagem em diferentes países.

---

### 5.7 Onde esses dados poderiam estar

Resumo — o detalhamento com URLs, formatos e método de coleta está em **§ 7.1**.

| Bloco | Onde está |
|---|---|
| A — Disponibilidade | Documentação técnica oficial de AWS Bedrock, Google Vertex AI e Microsoft Foundry; páginas oficiais de países suportados dos provedores; **repositório público de documentação da Microsoft no GitHub, que preserva histórico datado**; Internet Archive (Wayback Machine) para reconstruir o histórico das demais |
| B — Preço | Páginas oficiais de preço dos provedores e das três nuvens, com histórico via Wayback Machine |
| C — Controle | API pública da AWS de disponibilidade de serviços por região; páginas de infraestrutura global das três nuvens |
| D — Explicativas | Banco Mundial (World Development Indicators), União Internacional de Telecomunicações, Federal Register / Bureau of Industry and Security dos EUA, textos legais das jurisdições |
| E — Latência | Coleta própria a partir de máquinas em nuvem alocadas em diferentes países |

**Nenhuma dessas fontes exige contrato, credencial paga ou acesso privilegiado.** Todas foram verificadas como existentes e acessíveis em agosto de 2026.

---

## 6. Objetivos

**Objetivo geral**
Caracterizar e explicar a desigualdade geográfica na disponibilidade de modelos de IA generativa comercial de provedores estadunidenses, entre abril de 2024 e junho de 2026, distinguindo o efeito de fatores técnicos de maturidade de infraestrutura do efeito de fatores econômicos, regulatórios e geopolíticos.

**Objetivos específicos**

1. **Construir** uma base de dados longitudinal inédita, no formato modelo × região × plataforma × data, cobrindo disponibilidade, preço e recursos.
2. **Mensurar** a defasagem de disponibilidade e a taxa de cobertura de modelos por região, com intervalos de confiança.
3. **Descrever** o padrão geográfico e temporal da defasagem, verificando se a assimetria aumenta, diminui ou se mantém estável no período, **e comparar a defasagem dos serviços de IA com a defasagem geral da mesma região** (§ 7.5.2).
4. **Testar** a associação entre a defasagem e fatores econômicos, regulatórios e geopolíticos, **controlando pela maturidade da região de nuvem**, e discriminando entre as quatro hipóteses concorrentes de § 8.2.
5. **Posicionar** o Brasil no ordenamento resultante e avaliar se sua posição é compatível com seu porte econômico.

---

## 7. Plano de dados

### 7.1 Fontes verificadas

Todas as URLs abaixo foram checadas em **28 de agosto de 2026**. As marcadas ⚠️ exigem confirmação adicional pelo grupo (ver § 13).

#### Bloco A — Disponibilidade

| Fonte | O que fornece | Formato | Método |
|---|---|---|---|
| [AWS — Model support by AWS Region](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html) | Matriz modelo × região do Bedrock | HTML tabular | Raspagem |
| [Microsoft — Region availability for Foundry Models](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure-region-availability) | Matriz modelo × região do Foundry | HTML tabular | Raspagem |
| [MicrosoftDocs/azure-ai-docs no GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/blob/main/articles/foundry/foundry-models/concepts/models-sold-directly-by-azure-region-availability.md) | A mesma matriz, em Markdown, versionada | Markdown versionado | `git log` → data exata de cada alteração. ⚠️ **Histórico curto: o arquivo só existe desde maio/2026** (14 commits). Ver § 7.5 |
| [Microsoft — Feature availability across cloud regions](https://learn.microsoft.com/en-us/azure/foundry/reference/region-support) | Recursos por região | HTML | Raspagem |
| [Google Cloud — Locations do Vertex AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/locations) | Regiões e endpoints do Vertex | HTML | Raspagem |
| [Claude on Vertex AI](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai) | Modelos Claude por região do Vertex | HTML | Raspagem |
| [Anthropic — Supported countries & regions](https://www.anthropic.com/supported-countries) | Lista oficial de países atendidos | HTML | Raspagem |
| [modelavailability.com](https://modelavailability.com/platforms/gcp/regions) | Agregador de terceiros de disponibilidade por região | HTML | ⚠️ Usar **apenas** como validação cruzada, nunca como fonte primária — origem e método não auditáveis |

> ⚠️ **Correção importante, e é um bom exemplo do que a disciplina quer treinar.** A primeira versão deste documento afirmava que o repositório Git da Microsoft resolveria o problema da série histórica, por ser público e versionado. **Testamos, e a hipótese caiu:** o arquivo de disponibilidade regional só existe desde maio de 2026, com 14 commits — o repositório inteiro foi criado em agosto de 2024. O histórico é preciso, porém raso, e serve apenas aos últimos meses.
>
> A série histórica longa vem, na verdade, do **Internet Archive aplicado às páginas da AWS** (206 dias de snapshot desde março/2024) e à **página de países da Anthropic** (274 dias desde maio/2023). A Azure, que parecia a melhor fonte, é a pior. Os números medidos estão em § 7.5.
>
> **A lição metodológica vale ser dita na apresentação:** uma fonte de dados que parece ideal no papel precisa ser testada antes de virar premissa de cronograma. O slide 16 chama isso de teste de viabilidade.

#### Bloco A' — Reconstrução histórica

| Fonte | O que fornece | Formato | Método |
|---|---|---|---|
| **Internet Archive — API CDX** (`http://web.archive.org/cdx/search/cdx?url=...&output=json`) | Lista de todos os snapshots datados de uma URL | JSON | Requisição HTTP, depois busca de cada snapshot e *diff* entre eles |

#### Bloco C — Controle de maturidade de região *(bloco decisivo)*

| Fonte | O que fornece | Formato | Método |
|---|---|---|---|
| **`https://api.regional-table.region-services.aws.a2z.com/index.json`** | **Todos os serviços AWS × todas as regiões** | **JSON** | **Requisição HTTP direta** |
| [AWS — Regional Product Services](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/) | Versão navegável do mesmo dado | HTML | Validação |
| Páginas de infraestrutura global de AWS, Google e Microsoft | Data de lançamento e nº de zonas por região | HTML | Raspagem |

> Esse JSON é o que viabiliza o controle de confusão descrito em § 5.6. É a variável que impede o projeto de confundir "IA chega tarde no Brasil" com "tudo chega tarde no Brasil".

#### Bloco D — Variáveis explicativas

| Fonte | O que fornece | Acesso |
|---|---|---|
| Banco Mundial — World Development Indicators | PIB, PIB per capita, população, grupo de renda | API pública em JSON |
| União Internacional de Telecomunicações (UIT/ITU) — DataHub | Penetração de internet, indicadores de TIC | Download público |
| Federal Register / BIS (EUA) | Texto e datas das regras de controle de exportação de computação avançada | Público, com API |
| Textos legais das jurisdições | Vigência de GDPR, AI Act, LGPD e equivalentes | Codificação manual pelo grupo |

**Nota sobre a variável de controle de exportação — atenção, isso muda o desenho.** A chamada *AI Diffusion Rule*, publicada pelo BIS em **13 de janeiro de 2025**, criou uma classificação de países em três camadas de restrição, e foi **rescindida em 13 de maio de 2025**, imediatamente antes de entrar em vigor em 15 de maio. As camadas foram eliminadas.

Isso não é um problema — **é uma oportunidade metodológica**. Existe uma janela de quatro meses em que uma classificação oficial de países esteve publicada e depois foi revogada. Isso permite (i) usar a classificação original como variável explicativa mesmo tendo sido revogada, já que ela revela como o governo dos EUA agrupava países, e (ii) testar se houve mudança de comportamento das empresas em torno dessas duas datas — um desenho quase-experimental. Ver § 8.4.

#### Bloco E — Extensão opcional

| Fonte | O que fornece | Acesso |
|---|---|---|
| Máquinas de nuvem alocadas em diferentes países pelo grupo | Latência p50/p95 medida | Camada gratuita / crédito acadêmico |
| Benchmarks públicos de terceiros (ex.: Artificial Analysis) | Latência e vazão por modelo | ⚠️ Verificar se desagrega por região — provavelmente não |

### 7.2 Dicionário de dados preliminar

**Tabela `disponibilidade` — grão: modelo × região × plataforma**

| Campo | Tipo | Descrição |
|---|---|---|
| `id_modelo` | texto | Identificador canônico do modelo |
| `provedor` | categórico | Anthropic, OpenAI, Google |
| `plataforma` | categórico | AWS Bedrock, Vertex AI, Microsoft Foundry, API direta |
| `id_regiao` | texto | Código da região (`us-east-1`, `sa-east-1`, ...) |
| `pais_regiao` | texto | ISO 3166-1 alfa-2 |
| `data_lancamento_global` | data | 1ª disponibilidade em qualquer região |
| `data_disponibilidade_regiao` | data | 1ª disponibilidade nessa região; nulo se nunca |
| `defasagem_dias` | inteiro | **Desfecho primário.** `data_disponibilidade_regiao − data_lancamento_global` |
| `censurado` | booleano | Verdadeiro se o modelo nunca chegou à região até o fim da observação |
| `fonte` | texto | URL de origem |
| `data_coleta` | data-hora | Quando o registro foi coletado |
| `hash_snapshot` | texto | Hash do HTML/Markdown bruto arquivado — garante reprodutibilidade |

**Tabela `regiao` — grão: região**

| Campo | Tipo | Descrição |
|---|---|---|
| `id_regiao` | texto | Chave |
| `data_lancamento_regiao` | data | Quando a região abriu |
| `idade_regiao_anos` | decimal | Derivada, no momento do lançamento de cada modelo |
| `n_zonas_disponibilidade` | inteiro | Proxy de porte |
| `n_servicos_total` | inteiro | **Variável de controle central** — maturidade da região |
| `bloco_geoeconomico` | categórico | EUA / Aliados próximos / Demais |
| `regime_regulatorio` | categórico | GDPR-AI Act / LGPD / Outro / Sem lei geral |
| `camada_diffusion_rule` | categórico | Tier 1/2/3 conforme a regra de jan/2025, ainda que revogada |

**Tabela `pais` — grão: país** — PIB, PIB per capita, população, grupo de renda, penetração de internet, atendido por cada provedor (booleano), data de entrada na lista.

### 7.3 Definições operacionais (evitam ambiguidade na banca)

- **Modelo elegível:** modelo de linguagem de propósito geral, acesso comercial por API, dos provedores Anthropic, OpenAI ou Google, lançado entre 01/04/2024 e 30/06/2026. Excluem-se modelos exclusivamente de imagem, áudio, embedding e versões de pré-visualização não comercializadas.
- **Disponível em uma região:** consta como suportado na documentação oficial da plataforma para aquela região, em modo de inferência sob demanda. Não conta disponibilidade apenas por endpoint global ou multirregional — o endpoint global roteia para onde houver capacidade e por isso **não** caracteriza disponibilidade local.
- **Defasagem:** dias corridos entre `data_lancamento_global` e `data_disponibilidade_regiao`.
- **Região dos EUA:** região de nuvem cujo território físico está nos Estados Unidos, excluídas regiões governamentais de acesso restrito.

### 7.4 Estratégia de busca bibliográfica (aplicação direta de Santos et al., 2007)

O artigo prescreve: (i) selecionar descritores controlados e não-controlados por componente do PICO, (ii) combiná-los com operadores booleanos — `OR` aditivo dentro do componente, `AND` restritivo entre componentes, `NOT` excludente —, e (iii) montar a estratégia final `(P) AND (I) AND (C) AND (O)`.

**Adaptação necessária:** os vocabulários controlados citados no artigo — MeSH, DeCS, EMTREE — são da saúde e não se aplicam. Os equivalentes na Computação são o **ACM Computing Classification System** e o **IEEE Thesaurus**. Isso deve ser declarado na metodologia.

**Bases a consultar:** Scopus, Web of Science, ACM Digital Library, IEEE Xplore, arXiv (cs.CY, econ.GN), SSRN; e, em português, SciELO e BDTD.

**Strings por componente:**

```
P = ("large language model" OR "LLM" OR "foundation model" OR "generative AI"
     OR "AI model" OR "machine learning as a service" OR "cloud computing")

E = ("regional availability" OR "geographic availability" OR "service availability"
     OR "data residency" OR "digital sovereignty" OR "AI sovereignty"
     OR "export control" OR "technology transfer" OR "geopolitic*")

O = ("technology diffusion" OR "adoption lag" OR "time to availability"
     OR "digital divide" OR "digital inequality" OR "access gap"
     OR "pricing disparity" OR "latency")
```

**Estratégia final:**

```
(P) AND (E) AND (O)
    NOT ("federated learning" OR "edge computing" OR "network topology")
Filtros: 2019–2026; artigos, atas de conferência e preprints
```

> **Nota sobre o componente C.** O artigo admite que a comparação pode ser "nenhuma intervenção". Em revisão exploratória sobre tema emergente, incluir C na string reduz demais a recuperação. **C fica implícito na busca e explícito no desenho do estudo** — e isso deve ser declarado, não escondido.

**String em português, para SciELO e BDTD:**

```
("inteligência artificial generativa" OR "modelo de linguagem" OR "computação em nuvem")
AND ("soberania digital" OR "soberania de dados" OR "dependência tecnológica"
     OR "disponibilidade regional" OR "controle de exportação")
AND ("difusão tecnológica" OR "desigualdade digital" OR "assimetria de acesso")
```

**Registro obrigatório:** para cada base, anotar data da busca, string exata, nº de retornos, nº após triagem por título/resumo e nº após leitura integral. Sem isso, a revisão é narrativa — e o artigo é explícito ao criticar revisões narrativas por serem "tendenciosas" e "inconclusivas".

---

## 7.5 Teste de viabilidade das fontes — **executado**

O slide 16 estabelece: *"Se vocês não conseguem apontar onde estão os dados, ainda não têm uma pergunta de pesquisa."* Apontar não basta — apontamos e **medimos**. Os resultados abaixo foram obtidos em **28 de agosto de 2026** consultando diretamente as APIs das fontes.

### 7.5.1 Cobertura histórica medida (API CDX do Internet Archive)

Contagem de **dias distintos com snapshot** por trimestre. Esta tabela é o insumo que define a janela de observação do estudo.

| Fonte | 1º snapshot | Dias com snapshot | 2024 Q1·Q2·Q3·Q4 | 2025 Q1·Q2·Q3·Q4 | 2026 Q1·Q2 | Veredito |
|---|---|---|---|---|---|---|
| **Anthropic — países atendidos** | **2023-05-12** | **274** | 6·17·13·17 | 32·23·31·57 | 24·27 | ✅ **Excelente** — a melhor série do projeto |
| **AWS — `models-regions`** | 2024-03-05 | 206 | 2·4·1·8 | 11·13·19·54 | 53·29 | ✅ **Boa** — densa a partir de 2024 Q4 |
| **AWS — `models-supported`** | 2024-03-07 | 208 | 1·8·4·20 | 16·12·20·46 | 36·31 | ✅ **Boa** — usar como fonte redundante |
| Google — Vertex `locations` | 2024-04-22 | 44 | 0·5·2·4 | 7·6·7·7 | 5·0 | ⚠️ **Limitada** — ~1 snapshot/mês |
| Azure — `models-featured` | 2025-03-13 | 20 | 0·0·0·0 | 4·7·3·5 | 0·1 | ❌ **Insuficiente** para série histórica |
| Azure — histórico Git | arquivo: 2026-05-08 | 14 commits | — | — | — | ❌ **Raso** — repositório criado em ago/2024 |

**Três consequências diretas para o desenho:**

1. **A janela original de janeiro de 2023 é inviável e foi abandonada.** Nenhuma fonte de disponibilidade regional tem registro anterior a março de 2024. A janela do desfecho primário passa a ser **abril de 2024 – junho de 2026**.
2. **O desfecho de atendimento por país foi promovido a co-primário.** É o único com três anos de série densa, e responde diretamente à leitura (a) do § 2 — *o país simplesmente não é atendido*.
3. **A hierarquia de plataformas se inverteu.** A Azure, que parecia a fonte ideal por ser versionada em Git, é a mais fraca. A AWS é a espinha dorsal do estudo. Se for preciso cortar escopo, **corta-se a Azure, não a AWS.**

### 7.5.2 Variável de controle de maturidade de região — **confirmada e já obtida**

O endpoint `https://api.regional-table.region-services.aws.a2z.com/index.json` respondeu em JSON, com **1,3 MB**, contendo:

- **5.836** pares serviço × região
- **37** regiões AWS distintas
- Confirmado que **Amazon Bedrock consta em `sa-east-1` (São Paulo)**

Contagem de serviços por região — **esta é a variável de controle central do § 8.3**:

| Região | Nº de serviços |
|---|---|
| `us-east-1` (Norte da Virgínia) | **195** |
| `us-west-2` (Oregon) | 192 |
| `ap-southeast-2` (Sydney) | 190 |
| `eu-west-1` (Irlanda) | 189 |
| **`sa-east-1` (São Paulo)** | **170** |
| `ap-southeast-6` | 119 |
| `ap-east-2` | 115 |
| `eusc-de-east-1` | 105 |

**Por que este número decide o projeto.** São Paulo tem 170 dos 195 serviços de `us-east-1` — cerca de **87%**. Isso significa que a região brasileira já é estruturalmente defasada em relação à referência americana, **para todo e qualquer serviço da AWS, não só para IA**.

Logo, se o estudo encontrar que modelos de IA chegam com atraso a São Paulo, **isso não prova nada por si só** — parte do atraso é a defasagem geral da região. A pergunta correta, e agora mensurável, é: **o atraso da IA é maior do que os 13% de defasagem geral da região?** Se for, existe um efeito específico de IA. Se não for, a hipótese H4 do grupo cai e o fenômeno é maturidade de infraestrutura (H1).

Essa comparação virou a **pergunta secundária nº 4** do § 5.5, e é provavelmente o achado mais forte que o trabalho pode produzir.

### 7.5.3 Notas operacionais da coleta

- A API CDX exige **HTTPS**; requisições em `http://` sem seguir redirecionamento retornam corpo vazio — erro silencioso que custou tempo e vale registrar.
- O Internet Archive aplica limitação de taxa e devolve, em HTML, uma página *"Temporarily Offline"* em vez de erro HTTP. **O coletor precisa checar se a resposta começa com `[`** antes de tentar interpretá-la como JSON; caso contrário falha de forma confusa.
- Usar `collapse=timestamp:8` para reduzir a um snapshot por dia, e recuar com espera progressiva entre requisições.

---

## 8. Metodologia

### 8.1 Classificação do estudo

Estudo **observacional, longitudinal retrospectivo**, com componente descritivo e componente analítico, baseado em dados secundários públicos de natureza institucional.

Não é experimento: não há atribuição aleatória e não controlamos a exposição. **Consequência direta e inegociável: os resultados serão de associação, jamais de causalidade.** Toda redação de resultado deve dizer "está associado a", nunca "causa" ou "porque a empresa quis".

### 8.2 Hipóteses concorrentes — é aqui que o "por quê" original volta

Cada hipótese faz uma predição diferente e falseável. É a comparação entre elas que responde à curiosidade que originou o projeto.

| | Hipótese | Mecanismo proposto | Predição verificável | Como seria refutada |
|---|---|---|---|---|
| **H1** | **Capacidade / infraestrutura** | Defasagem reflete escassez de hardware acelerado e maturidade da região | Após controlar por `n_servicos_total` e `idade_regiao_anos`, o efeito de bloco geoeconômico **desaparece** | Efeito de bloco persiste após controle |
| **H2** | **Mercado** | Provedores priorizam regiões de maior retorno esperado | PIB e gasto em TI são os preditores dominantes; o efeito de bloco é mediado por eles | PIB não prediz, ou prediz fracamente |
| **H3** | **Regulatória** | Exigências de residência de dados e conformidade impõem custo de entrada | UE atrasa **apesar** de PIB alto; regiões com regime rigoroso atrasam mais, controlando por renda | UE não difere de outras regiões ricas |
| **H4** | **Geopolítica** | Alinhamento com EUA e controles de exportação condicionam o acesso | Efeito de bloco e de camada de controle de exportação **persiste** após todos os controles | Efeito some com os controles |

> **A hipótese que o grupo trouxe é a H4.** O desenho a coloca em competição com três alternativas plausíveis, e H1 é a mais provável de vencer em boa parte dos casos. **Se H1 vencer, o projeto deve dizer isso com todas as letras.** Um projeto que só sabe confirmar não é pesquisa.

### 8.3 Estratégia de análise — derivada do desfecho, não escolhida antes

Seguindo a regra do slide 5, a técnica vem depois. O desfecho primário é **tempo até um evento, com censura à direita** — muitas regiões nunca receberam certos modelos até o fim da janela de observação, e descartá-las enviesaria o resultado exatamente na direção que queremos evitar. Esse formato de desfecho determina o método:

**Etapa 1 — Descritiva**
Cobertura de modelos por região; distribuição da defasagem por bloco; mapa coroplético de cobertura; curvas de difusão acumulada por região ao longo de 2023–2026; tabela de posição do Brasil.

**Etapa 2 — Estimador não paramétrico**
Curvas de Kaplan-Meier da probabilidade de um modelo ter chegado a uma região em função do tempo desde o lançamento global, estratificadas por bloco geoeconômico. Teste de log-rank para diferença entre estratos. Responde "existe diferença?" sem assumir forma funcional.

**Etapa 3 — Modelo multivariado**
Regressão de riscos proporcionais de Cox, com o desfecho "tempo até disponibilidade", incluindo:
- variáveis de exposição: bloco geoeconômico, regime regulatório, camada de controle de exportação;
- **controles obrigatórios: `n_servicos_total`, `idade_regiao_anos`, `n_zonas_disponibilidade`**;
- controles econômicos: log do PIB, PIB per capita;
- efeitos fixos de plataforma e de modelo, para absorver diferenças de política entre provedores e de porte entre modelos;
- erros-padrão agrupados por região.

Verificação do pressuposto de riscos proporcionais por resíduos de Schoenfeld; se violado, modelo com efeito dependente do tempo.

**Etapa 4 — Desfechos secundários**
Regressão logística para atendimento ao país (sim/não); regressão para diferencial de preço; modelo de contagem para nº de recursos habilitados por região.

**Etapa 5 — Robustez**
Reestimação excluindo cada provedor por vez; excluindo a China (caso extremo que pode dominar o efeito); com definições alternativas de "disponível"; e com janelas temporais alternativas.

> **Nenhuma dessas escolhas é decorativa.** Kaplan-Meier e Cox estão aqui porque o desfecho é tempo-até-evento com censura — se o desfecho fosse binário, seriam logística e nada mais. Essa justificativa deve constar da metodologia escrita.

### 8.4 Componente quase-experimental (opcional, alto valor)

A *AI Diffusion Rule* foi publicada em 13/01/2025 e rescindida em 13/05/2025. Se a base tiver granularidade suficiente, é possível testar se houve mudança no ritmo de disponibilização regional em torno dessas duas datas, comparando regiões de camadas diferentes antes e depois. É um desenho de diferenças-em-diferenças e seria o achado mais forte do trabalho.

⚠️ **Condição de viabilidade:** exige nº suficiente de eventos de disponibilização em cada janela. **Verificar depois da coleta, nunca antes.** Se os dados não sustentarem, abandonar sem constrangimento e registrar por quê.

### 8.5 Extensão opcional — medição de latência

Alocar máquinas em ~6 países (EUA, Brasil, Alemanha, Índia, Japão, África do Sul), emitir um conjunto padronizado de requisições idênticas ao mesmo modelo, e registrar latência p50/p95 e vazão de tokens. Controlar por horário e por tamanho de requisição.

⚠️ Só entra se o núcleo (§ 8.3) estiver concluído. Custa dinheiro e tempo, e é a parte mais fácil de fazer mal.

### 8.6 Reprodutibilidade

Todo HTML/JSON bruto coletado deve ser arquivado com data e hash. O código de coleta, limpeza e análise fica versionado. A base final é publicada junto com o trabalho. Sem isso, ninguém consegue verificar — e o argumento inteiro depende de ser verificável.

---

## 9. Riscos e ameaças à validade

### 9.1 Validade de construto

**"Disponibilidade documentada" não é "acesso real".** Um modelo pode constar como disponível numa região e, na prática, exigir aprovação, ter cota zero ou não ter capacidade. O construto medido é *disponibilidade documentada*, e isso precisa ser dito explicitamente na redação — não é o mesmo que acesso efetivo.
**Mitigação:** triangular com páginas de status e, se a extensão § 8.5 for feita, com medição direta.

### 9.2 Viés de sobrevivência documental

Páginas de documentação são reescritas, e a versão anterior desaparece. A cobertura do Internet Archive é irregular: URLs populares têm snapshots frequentes, outras têm meses de lacuna.
**Esta ameaça foi quantificada, não apenas prevista** — ver § 7.5.1. A densidade varia de 274 dias de snapshot (Anthropic) a 20 dias (Azure).
**Mitigação:** ancorar o desfecho primário na AWS (206–208 dias) e o co-primário na Anthropic (274 dias); tratar Google como parcialmente observado; **excluir a Azure do componente longitudinal** e usá-la apenas na análise transversal; publicar a tabela de densidade de snapshots junto com os resultados; testar sensibilidade à exclusão das fontes mal cobertas.
**Efeito residual:** a granularidade temporal do desfecho é limitada pelo intervalo entre snapshots. Em 2024 Q3 há apenas 1 snapshot da AWS — a defasagem naquele trimestre tem incerteza de até ~90 dias. Isso deve ser reportado como intervalo, nunca como data pontual.

### 9.3 Confusão por maturidade de região

A ameaça mais séria. Já tratada em § 5.6 e § 8.3, e é a razão de o Bloco C ser obrigatório.

### 9.4 Descasamento entre unidades região e país

Uma região de nuvem atende muitos países; um país pode não ter região alguma. Tratar região como se fosse país é erro de agregação.
**Mitigação:** dois níveis de análise separados — região para defasagem, país para atendimento e preço — nunca misturados na mesma regressão.

### 9.5 Endogeneidade

Provedores abrem regiões onde há demanda; a demanda cresce onde há região. Correlação entre PIB e disponibilidade é, em parte, causalidade reversa.
**Mitigação:** não há solução completa sem variável instrumental. **A honestidade é a mitigação:** declarar a limitação e não afirmar causalidade.

### 9.6 Risco de viés de confirmação do próprio grupo

O grupo parte de uma hipótese com carga política. O risco de ler os dados na direção desejada é real.
**Mitigação:** registrar as quatro hipóteses e suas predições **antes** de rodar a análise (§ 8.2), e apresentar todos os resultados, inclusive os que contrariam H4.

### 9.7 Instabilidade do objeto

O objeto muda durante a pesquisa: modelos são lançados e descontinuados, regiões abrem, regras mudam.
**Mitigação:** congelar a janela de observação em 30/06/2026 e não estendê-la, ainda que apareça notícia nova durante a escrita.

---

## 10. Considerações éticas e de conformidade

| Aspecto | Situação |
|---|---|
| Dados pessoais | **Nenhum.** Todas as unidades de análise são institucionais — modelos, regiões, países, empresas. Não há sujeito humano |
| Submissão a comitê de ética | Não aplicável, pela razão acima |
| Legalidade da coleta | Documentação técnica pública. Respeitar `robots.txt`, limitar taxa de requisição, identificar o agente de coleta e não sobrecarregar servidores |
| Termos de uso | Verificar os ToS de cada site antes de raspar; o Internet Archive tem uso acadêmico expressamente permitido |
| Uso de fontes de terceiros | Agregadores não auditáveis (ex.: modelavailability.com) apenas para validação cruzada, nunca como fonte primária |
| Redação dos achados | Formular como associação. **Não atribuir intenção, discriminação deliberada ou má-fé a empresas nomeadas** sem evidência direta — que não teremos |
| Transparência de conflito | ⚠️ **Declarar no trabalho:** parte do apoio à construção deste projeto foi feita com uma ferramenta de IA da Anthropic, que é uma das empresas estudadas. Isso não invalida nada, porque toda a análise se apoia em dados públicos verificáveis por terceiros — mas omitir seria desonesto |

---

## 11. Cronograma

Semanas relativas ao início do semestre. Ajustar às datas reais do plano de ensino.

| Semanas | Etapa (slide 4) | Entregas |
|---|---|---|
| 1 | tema | Cartão, formação do grupo, registro no formulário |
| 2 | problema | **Ficha Inicial v1** — este documento |
| 3–4 | pergunta / objetivos | Ficha v2 com pergunta refinada após feedback; PICOC fechado |
| 5–6 | revisão | Execução das strings de § 7.4; triagem; fichamento de 15–25 trabalhos; referencial teórico |
| 7 | metodologia | Protocolo metodológico escrito, hipóteses **registradas antes da análise** |
| 8–10 | dados | Coletores implementados; base construída; controle de qualidade; dicionário de dados final |
| 11 | dados | Marco crítico: base congelada e validada. **Se a coleta falhar, é aqui que se replaneja — não depois** |
| 12–13 | análise | Descritiva; Kaplan-Meier; Cox; desfechos secundários |
| 14 | análise | Robustez; decisão sobre § 8.4; consolidação de figuras e tabelas |
| 15 | resultados | Redação do artigo; discussão frente às quatro hipóteses; limitações |
| 16 | apresentação | Apresentação final; publicação de código e base |

**Caminho crítico:** semanas 8–11.

**O plano B foi reescrito após o teste de § 7.5**, que inverteu o diagnóstico inicial. A hierarquia real de robustez das fontes é:

1. **Anthropic — países atendidos** (274 dias, desde mai/2023) — a mais sólida. Sustenta sozinha o desfecho co-primário.
2. **AWS Bedrock** (206–208 dias, desde mar/2024) — espinha dorsal do desfecho primário.
3. **Google Vertex** (44 dias) — complementar, com incerteza temporal maior.
4. **Azure** (20 dias no Wayback; Git desde mai/2026) — **fora do componente longitudinal**; entra só na análise transversal.

**Se a coleta falhar na semana 11**, o recuo é para o desfecho co-primário — atendimento por país —, que depende de uma única fonte, é o mais denso e é o mais próximo da pergunta original do grupo. Um projeto inteiro e defensável cabe só nele. A decisão é da semana 10, no máximo.

---

## 12. Atividade individual — o cartão (slide 17)

Formato: *"Eu gostaria de entender por que ____"* + uma segunda linha dizendo por que isso incomoda ou interessa.
Regra única: **proibido escrever nome de técnica.** Nenhuma das versões abaixo contém.

**Versão A**
> Eu gostaria de entender por que as ferramentas de inteligência artificial mais avançadas chegam mais tarde, mais caras e com menos recursos para quem trabalha fora dos Estados Unidos.
> Isso me incomoda porque decide, sem que ninguém tenha votado nisso, quem consegue construir com a tecnologia da fronteira e quem só consegue consumi-la com atraso.

**Versão B**
> Eu gostaria de entender por que uma empresa brasileira e uma empresa americana, pagando o mesmo preço pelo mesmo serviço de inteligência artificial, não recebem o mesmo serviço.
> Isso me interessa porque é uma desigualdade que ninguém mede, e o que não se mede não entra em nenhuma discussão séria de política pública.

**Versão C**
> Eu gostaria de entender por que a distância física até um data center americano ainda determina o que uma empresa consegue construir em 2026.
> Isso me incomoda porque a promessa da nuvem era justamente que o lugar de onde você trabalha deixaria de importar — e aparentemente ainda importa.

---

## 13. Pendências de verificação ⚠️

Itens que **o grupo deve confirmar** antes da entrega. Nenhum invalida o projeto, mas todos afetam o planejamento.

Itens 1 e 2 **já foram testados** e estão resolvidos (§ 7.5). Os demais permanecem com o grupo.

| # | Item | Situação | Resultado / como verificar |
|---|---|---|---|
| 1 | Densidade de snapshots do Internet Archive | ✅ **RESOLVIDO** | Medida fonte a fonte em § 7.5.1. Anthropic 274 dias, AWS 206–208, Google 44, Azure 20. **Janela do estudo foi encurtada para abr/2024 em consequência** |
| 2 | Profundidade do histórico Git da documentação Microsoft | ✅ **RESOLVIDO — hipótese refutada** | Arquivo criado em 08/05/2026, 14 commits; repositório criado em ago/2024. Insuficiente para série histórica. **Azure saiu do componente longitudinal** |
| 3 | Situação atual dos controles de exportação dos EUA | ⚠️ **Parcial** | Confirmado: regra publicada em 13/01/2025, rescindida em 13/05/2025, camadas eliminadas. **Falta confirmar se houve regra substituta após mai/2025** — consultar o Federal Register |
| 4 | Se as páginas oficiais de preço desagregam por região | ⬜ Pendente | Inspecionar as páginas de preço dos três provedores e das três nuvens |
| 5 | Histórico da lista de países da OpenAI | ⬜ Pendente | Mesmo método de § 7.5.1 aplicado à URL da OpenAI. *(A da Anthropic já está confirmada: 274 dias desde mai/2023)* |
| 6 | `robots.txt` e termos de uso de cada domínio | ⬜ Pendente | Ler `/robots.txt` de cada domínio antes de escrever o coletor |
| 7 | Nº de eventos de disponibilização em torno de jan e mai/2025 | ⬜ Pendente | Só após a base construída, semana 11. Define se § 8.4 é viável |
| 8 | Norma de formatação exigida (ABNT ou outra) | ⬜ Pendente | Perguntar ao professor |
| 9 | **Confirmar a data de lançamento global de cada modelo** | ⬜ **Novo — crítico** | É o marco zero da defasagem. Blogs oficiais dos provedores e notas de versão. Sem essa data, o desfecho primário não existe |

---


## 14. Referências

SANTOS, C. M. C.; PIMENTA, C. A. M.; NOBRE, M. R. C. **A estratégia PICO para a construção da pergunta de pesquisa e busca de evidências**. *Revista Latino-Americana de Enfermagem*, v. 15, n. 3, maio–jun. 2007.

GOMES, R. R. **Projeto em Ciência de Dados IV — Aula 01: Da curiosidade à pergunta investigável**. PUC Minas, 2º semestre de 2026.

BERGIN, S. M.; WRAIGHT, P. **Silver based wound dressings and topical agents for treating diabetic foot ulcers**. *Cochrane Database of Systematic Reviews*, 2006, n. 1, CD005082. *(citado em Santos et al. como exemplo de aplicação do PICO)*

KITCHENHAM, B.; CHARTERS, S. **Guidelines for performing Systematic Literature Reviews in Software Engineering**. Technical Report EBSE-2007-01, 2007. *(origem da extensão PICOC usada em § 4.2 — verificar edição atual)*

Fontes de dados: listadas com URL em § 7.1.

---

*Documento gerado em 28 de agosto de 2026. Versão 1 — sujeito a revisão após feedback em aula, conforme o slide 20: o tema não está congelado e a pergunta não precisa estar perfeita.*
