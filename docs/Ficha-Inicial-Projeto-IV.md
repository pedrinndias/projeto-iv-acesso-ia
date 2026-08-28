# Ficha Inicial do Projeto e Escopo de Pesquisa

## 1. Ficha Inicial do Projeto

### 1.1 Área de interesse

Ciência de dados aplicada a políticas de tecnologia e desigualdade digital, na interseção entre economia da computação em nuvem, difusão de tecnologia e geopolítica da inteligência artificial.

### 1.2 Tema inicial

Desigualdade geográfica no acesso a modelos de inteligência artificial generativa comercial.

### 1.3 Problema de pesquisa

Modelos de IA generativa deixaram de ser curiosidade técnica e passaram a ser insumo produtivo: empresas, hospitais, universidades e órgãos públicos constroem sistemas sobre eles. Esse insumo é ofertado por um pequeno número de empresas concentradas em um único país, e não chega a todos os lugares ao mesmo tempo, pelo mesmo preço, nem com os mesmos recursos.

Existe percepção difundida, entre desenvolvedores e empresas fora dos Estados Unidos, de que o acesso a esses modelos é sistematicamente pior fora do território americano: chega depois, custa mais, oferece menos recursos e, em alguns países, não chega. Essa percepção não está quantificada. Não se sabe o tamanho da defasagem, se ela é uniforme entre regiões, se vem aumentando ou diminuindo, nem se ela se explica por fatores técnicos neutros — uma região de nuvem recente ainda não tem capacidade instalada e recebe todos os serviços com atraso — ou por fatores econômicos, regulatórios e geopolíticos que operariam especificamente sobre inteligência artificial.

Enquanto essa distinção não for feita com dados, a discussão sobre soberania digital e dependência tecnológica permanece apoiada em relatos isolados, e empresas brasileiras que precisam decidir onde hospedar sistemas de IA decidem sem parâmetro.

### 1.4 Justificativa

**Relevância prática.** A adoção de IA generativa no Brasil cresce, e a decisão de arquitetura — usar uma região local com menos modelos disponíveis, ou uma região americana com melhor oferta mas com implicações de residência de dados sob a LGPD — é hoje tomada sem métrica. Quantificar a defasagem transforma essa decisão em cálculo.

**Relevância para política pública.** O debate sobre soberania de IA, data centers nacionais e regulação de inteligência artificial no Brasil se beneficia de evidência sobre a magnitude real da assimetria de acesso. Medir é pré-requisito para decidir se há algo a corrigir.

**Relevância científica.** Há literatura consolidada sobre difusão de tecnologia e sobre divisão digital em termos de infraestrutura e conectividade. Há muito menos trabalho medindo assimetria de acesso à camada de computação de inteligência artificial, que é uma forma nova de divisão digital: opera não sobre quem tem internet, mas sobre quem tem acesso à fronteira da capacidade computacional. O projeto se posiciona nessa lacuna.

**Delimitação de risco.** É possível que os resultados contrariem a hipótese inicial do grupo, e que a defasagem se explique por maturidade de infraestrutura em vez de fatores geopolíticos. O desenho foi construído para permitir esse resultado, e nesse caso ele será relatado como tal.

### 1.5 Pergunta de pesquisa

**Pergunta principal**

> Quais fatores estão associados à defasagem de disponibilidade regional de modelos de IA generativa comercial de provedores estadunidenses (Anthropic, OpenAI e Google), nas plataformas AWS Bedrock, Google Vertex AI e Microsoft Foundry, entre abril de 2024 e junho de 2026?

**Pergunta co-primária**

> Quais características dos países estão associadas à sua ausência das listas oficiais de atendimento dos provedores de IA estadunidenses, e como essa composição mudou entre maio de 2023 e junho de 2026?

**Perguntas secundárias**

1. Qual a magnitude da defasagem mediana de disponibilidade entre regiões dos Estados Unidos e regiões fora dos Estados Unidos, e como ela evoluiu no período?
2. Existe diferença de preço, para o mesmo modelo e mesmo volume, entre regiões dentro e fora dos Estados Unidos?
3. Em que posição o Brasil se situa no ordenamento de defasagem, e essa posição é compatível com seu porte econômico?
4. A defasagem dos serviços de IA é maior do que a defasagem dos demais serviços de nuvem na mesma região, isto é, existe atraso específico de IA além do atraso geral de infraestrutura?

As janelas temporais das duas perguntas principais são diferentes porque a disponibilidade das fontes históricas é diferente. A justificativa está na seção 3.

### 1.6 Que dados seriam necessários

**Bloco A — Disponibilidade.** Matriz modelo por região por plataforma, com indicação de disponibilidade em cada data; data da primeira disponibilidade global de cada modelo, que é o marco zero da defasagem; data de entrada de cada modelo em cada região; lista de países atendidos por cada provedor, com histórico de alterações; recursos habilitados por modelo e região.

**Bloco B — Preço.** Preço por milhão de tokens de entrada e de saída, por modelo, região e data.

**Bloco C — Controle de maturidade da região.** Data de lançamento da região de nuvem, número de zonas de disponibilidade e número total de serviços da plataforma disponíveis naquela região.

Este bloco é condição de interpretabilidade de todo o estudo. Se um modelo demora a chegar a São Paulo, mas todos os serviços da mesma plataforma demoram a chegar a São Paulo, o atraso é maturidade de infraestrutura e não tratamento diferenciado à inteligência artificial. Sem essa variável, qualquer associação encontrada seria ambígua.

**Bloco D — Variáveis explicativas do país.** PIB, PIB per capita, população e grupo de renda; indicadores de desenvolvimento de tecnologias de informação e comunicação; regime regulatório de proteção de dados vigente; situação frente a controles de exportação e sanções dos Estados Unidos, com as datas de mudança de política.

**Bloco E — Extensão opcional.** Latência medida a partir de pontos de observação em diferentes países.

### 1.7 Onde esses dados poderiam estar

| Bloco | Fonte |
|---|---|
| A — Disponibilidade | Documentação técnica oficial da AWS Bedrock, do Google Vertex AI e do Microsoft Foundry; páginas oficiais de países atendidos da Anthropic e da OpenAI; repositório público de documentação da Microsoft no GitHub |
| A' — Série histórica | Internet Archive (Wayback Machine), por meio da API CDX, aplicada às páginas acima |
| B — Preço | Páginas oficiais de preço dos provedores e das três plataformas de nuvem, com histórico via Internet Archive |
| C — Controle | Índice público de disponibilidade de serviços por região da AWS, em formato JSON; páginas de infraestrutura global das três plataformas |
| D — Explicativas | Banco Mundial (World Development Indicators); União Internacional de Telecomunicações; Federal Register e Bureau of Industry and Security dos Estados Unidos; textos legais das jurisdições |
| E — Latência | Coleta própria a partir de máquinas alocadas em diferentes países |

Nenhuma dessas fontes exige contrato, credencial paga ou acesso privilegiado. Todas foram verificadas pelo grupo como existentes e acessíveis em agosto de 2026, e a verificação está documentada na seção 3.

---

## 2. Construção da pergunta pela estratégia PICO

### 2.1 Do tema à pergunta

O tema surgiu de uma curiosidade formulada, inicialmente, como "por que as empresas de IA americanas limitam o processamento para empresas de fora dos Estados Unidos". Ao trabalhar essa formulação, o grupo identificou três obstáculos.

Primeiro, ela pressupõe o fenômeno em vez de medi-lo: afirma que há limitação antes de verificar se há, e de que tamanho. Segundo, uma pergunta sobre a intenção de uma empresa exigiria acesso a deliberações internas, que não estão disponíveis. Terceiro, "limitar o processamento" comporta pelo menos seis leituras distintas — o país não ser atendido, o modelo demorar a chegar à região, haver cota menor, haver latência maior, haver preço maior ou haver recursos ausentes — e sem escolher uma delas não existe variável de desfecho.

A reformulação adotada substitui a pergunta sobre intenção por uma pergunta sobre fenômeno mensurável e seus fatores associados. A questão de origem não é abandonada: ela retorna na forma de quatro hipóteses concorrentes, apresentadas na seção 5.2, cada uma com uma predição distinta e verificável.

Essa conversão segue o procedimento do artigo de referência da disciplina. Santos, Pimenta e Nobre (2007) relatam que a revisão sistemática de Bergin e Wraight nasceu do questionamento sobre o porquê da não utilização de curativos com prata, e que a pergunta efetivamente construída com o PICO foi qual o efeito desses curativos no tratamento de úlceras de pé em diabéticos. O movimento é o mesmo: de uma pergunta sobre motivo para uma pergunta sobre efeito mensurável.

O grupo considerou dez recortes possíveis antes de fixar este. Três deles — diferencial de preço entre regiões, ausência de países nas listas de atendimento e restrição de recursos por região — foram incorporados como desfechos secundários, por virem das mesmas fontes já necessárias ao desfecho principal. Os demais foram descartados por inviabilidade de dados ou por exigirem método que não é o desta disciplina.

### 2.2 Adaptação do PICO para PICOC

O PICO foi formulado na área da saúde, onde o componente I designa uma intervenção administrada pelo pesquisador. Em estudo observacional não há intervenção, e sim exposição. Duas adaptações consagradas cobrem esse caso e ambas foram aplicadas: o PECO, que substitui *Intervention* por *Exposure* e é padrão em epidemiologia observacional; e o PICOC, que acrescenta *Context* e é a adaptação usada em revisões sistemáticas na área de Computação, conforme a metodologia de Kitchenham.

### 2.3 Componentes do PICOC neste projeto

| Componente | Definição original | Neste projeto |
|---|---|---|
| P — População | Paciente, grupo de pacientes ou problema | Unidade de análise: o par formado por modelo de IA e região de nuvem. Modelos de linguagem de propósito geral, de acesso comercial por API, dos provedores Anthropic, OpenAI e Google. Unidade secundária: o par provedor e país |
| E — Exposição | Intervenção de interesse | Estar fora dos Estados Unidos, operacionalizado em três variáveis: bloco geoeconômico da região; regime regulatório de dados vigente; situação frente a controles de exportação dos Estados Unidos |
| C — Comparação | Intervenção padrão, ou nenhuma | Regiões de nuvem sediadas nos Estados Unidos, que funcionam como linha de base por serem onde os modelos costumam estrear |
| O — Desfecho | Resultado esperado | Primário: defasagem, em dias, entre a primeira disponibilidade documentada do modelo em qualquer região e sua disponibilidade naquela região, com censura à direita para regiões que nunca a receberam. Secundários: taxa de cobertura de modelos por região; atendimento ao país; preço por milhão de tokens; número de recursos habilitados |
| C — Contexto | Extensão PICOC | Plataformas AWS Bedrock, Google Vertex AI e Microsoft Foundry, e acesso direto pelas APIs dos provedores. Janela de abril de 2024 a junho de 2026 para o desfecho de disponibilidade regional, e de maio de 2023 a junho de 2026 para o desfecho de atendimento por país |

A pergunta da seção 1.5 resulta do encadeamento desses componentes.

---

## 3. Verificação de viabilidade das fontes

O material da disciplina estabelece que, sem saber apontar onde estão os dados, ainda não há pergunta de pesquisa. O grupo optou por não apenas apontar as fontes, mas medir sua cobertura antes de fixar o recorte temporal. As consultas foram feitas em 28 de agosto de 2026, diretamente às APIs das fontes.

### 3.1 Cobertura histórica das fontes

Contagem de dias distintos com registro arquivado, por trimestre, obtida pela API CDX do Internet Archive.

| Fonte | Primeiro registro | Dias arquivados | 2024 | 2025 | 2026 | Situação |
|---|---|---|---|---|---|---|
| Anthropic, países atendidos | 12/05/2023 | 274 | 53 | 143 | 51 | Adequada |
| AWS Bedrock, modelos por região | 05/03/2024 | 206 | 15 | 97 | 82 | Adequada |
| AWS Bedrock, modelos suportados | 07/03/2024 | 208 | 33 | 94 | 67 | Adequada |
| Google Vertex AI, localizações | 22/04/2024 | 44 | 11 | 27 | 5 | Limitada |
| Microsoft Foundry, modelos | 13/03/2025 | 20 | 0 | 19 | 1 | Insuficiente |
| Microsoft, histórico do repositório | 08/05/2026 | 14 registros | 0 | 0 | 14 | Insuficiente |

Essa medição produziu três decisões de desenho.

1. **A janela de observação começa em abril de 2024, e não em janeiro de 2023.** Nenhuma fonte de disponibilidade regional possui registro anterior a março de 2024. O recorte temporal foi definido pelo dado existente.
2. **O desfecho de atendimento por país foi promovido a co-primário.** É o único com três anos de série densa, e corresponde à leitura mais direta do problema descrito na seção 1.3.
3. **A plataforma Microsoft foi retirada do componente longitudinal.** A hipótese inicial do grupo era de que seu repositório público de documentação forneceria a melhor série histórica, por ser versionado. A verificação mostrou o contrário: o arquivo pertinente existe apenas desde maio de 2026. A AWS passou a ser a base do desfecho principal.

### 3.2 Variável de controle de maturidade da região

O índice público de disponibilidade de serviços da AWS foi obtido em formato JSON, com 1,3 MB, contendo 5.836 pares de serviço e região, distribuídos em 37 regiões. Confirmou-se que o Amazon Bedrock consta na região de São Paulo.

| Região | Serviços disponíveis |
|---|---|
| us-east-1 (Norte da Virgínia) | 195 |
| us-west-2 (Oregon) | 192 |
| ap-southeast-2 (Sydney) | 190 |
| eu-west-1 (Irlanda) | 189 |
| sa-east-1 (São Paulo) | 170 |
| ap-southeast-6 | 119 |
| ap-east-2 | 115 |
| eusc-de-east-1 | 105 |

São Paulo dispõe de 170 dos 195 serviços presentes na região de referência nos Estados Unidos, cerca de 87%. A região brasileira já é estruturalmente defasada para o conjunto dos serviços da plataforma, e não apenas para inteligência artificial.

Isso torna mensurável a comparação decisiva do estudo: verificar se o atraso dos modelos de IA é maior do que os aproximadamente 13% de defasagem geral da região. Se for, há efeito específico de inteligência artificial. Se não for, o fenômeno é explicado por maturidade de infraestrutura. Essa comparação corresponde à pergunta secundária número 4.

---

## 4. Objetivos

**Objetivo geral.** Caracterizar e explicar a desigualdade geográfica na disponibilidade de modelos de IA generativa comercial de provedores estadunidenses, entre abril de 2024 e junho de 2026, distinguindo o efeito de fatores técnicos de maturidade de infraestrutura do efeito de fatores econômicos, regulatórios e geopolíticos.

**Objetivos específicos**

1. Construir base de dados longitudinal no formato modelo, região, plataforma e data, cobrindo disponibilidade, preço e recursos.
2. Mensurar a defasagem de disponibilidade e a taxa de cobertura de modelos por região, com intervalos de confiança.
3. Descrever o padrão geográfico e temporal da defasagem, e compará-la com a defasagem geral da mesma região.
4. Testar a associação entre a defasagem e fatores econômicos, regulatórios e geopolíticos, controlando pela maturidade da região.
5. Posicionar o Brasil no ordenamento resultante e avaliar se sua posição é compatível com seu porte econômico.

---

## 5. Metodologia prevista

### 5.1 Classificação do estudo

Estudo observacional, longitudinal retrospectivo, com componente descritivo e componente analítico, baseado em dados secundários públicos de natureza institucional. Não há atribuição aleatória nem controle da exposição, de modo que os resultados serão de associação e não de causalidade.

### 5.2 Hipóteses concorrentes

| | Hipótese | Mecanismo | Predição verificável |
|---|---|---|---|
| H1 | Capacidade e infraestrutura | A defasagem reflete escassez de hardware e maturidade da região | Após controle pelo número de serviços e pela idade da região, o efeito de bloco geoeconômico desaparece |
| H2 | Mercado | Provedores priorizam regiões de maior retorno esperado | PIB e gasto em tecnologia são os preditores dominantes |
| H3 | Regulatória | Exigências de residência de dados impõem custo de entrada | A União Europeia atrasa apesar de PIB alto |
| H4 | Geopolítica | Alinhamento com os Estados Unidos e controles de exportação condicionam o acesso | O efeito de bloco persiste após todos os controles |

A hipótese de origem do grupo é a H4. O desenho a coloca em competição com três alternativas plausíveis. Caso a H1 prevaleça, esse será o resultado relatado.

### 5.3 Estratégia de análise

O desfecho principal é tempo até um evento, com censura à direita, uma vez que diversas regiões não haviam recebido determinados modelos até o fim da janela de observação. Descartar essas observações enviesaria o resultado. O formato do desfecho determina o método, e não o contrário.

1. **Análise descritiva.** Cobertura de modelos por região, distribuição da defasagem por bloco, representação cartográfica e curvas de difusão acumulada.
2. **Estimador não paramétrico.** Curvas de Kaplan-Meier estratificadas por bloco geoeconômico, com teste de log-rank.
3. **Modelo multivariado.** Regressão de riscos proporcionais de Cox, incluindo as variáveis de exposição; controles obrigatórios de número de serviços, idade da região e número de zonas de disponibilidade; controles econômicos; efeitos fixos de plataforma e de modelo; erros-padrão agrupados por região.
4. **Desfechos secundários.** Regressão logística para atendimento ao país, regressão para diferencial de preço e modelo de contagem para recursos habilitados.
5. **Robustez.** Reestimação excluindo cada provedor por vez, com definições alternativas de disponibilidade e com janelas temporais alternativas.

Todo material bruto coletado será arquivado com data e identificador, e o código de coleta e análise será versionado, de modo que os resultados possam ser verificados por terceiros.

---

## 6. Riscos e limitações

**Validade de construto.** O que se mede é disponibilidade documentada, que não equivale a acesso efetivo: um modelo pode constar como disponível e, na prática, exigir aprovação ou não ter capacidade alocada. A limitação será declarada nos resultados.

**Cobertura documental irregular.** A densidade de registros arquivados varia entre fontes, conforme a seção 3.1. Em trimestres com poucos registros, a defasagem terá incerteza de até noventa dias e será relatada como intervalo, nunca como data exata.

**Confusão por maturidade da região.** É a principal ameaça, e a razão de o Bloco C ser obrigatório.

**Endogeneidade.** Provedores abrem regiões onde há demanda, e a demanda cresce onde há região. Parte da correlação entre PIB e disponibilidade é de sentido inverso. Não há solução completa sem variável instrumental, e a limitação será declarada.

**Viés de confirmação.** O grupo parte de uma hipótese com carga política. Como controle, as quatro hipóteses e suas predições serão registradas antes da execução da análise, e todos os resultados serão apresentados.

**Aspectos éticos.** O estudo não utiliza dados pessoais: todas as unidades de análise são institucionais, o que dispensa submissão a comitê de ética. A coleta observará os arquivos de restrição e os termos de uso de cada domínio, com limitação de taxa de requisição. Os achados serão formulados como associação, sem atribuir intenção ou má-fé às empresas analisadas.

---

## 7. Cronograma

| Semanas | Etapa | Entregas |
|---|---|---|
| 1 | Tema | Formação do grupo e definição da área |
| 2 | Problema | Ficha Inicial do Projeto |
| 3 e 4 | Pergunta e objetivos | Pergunta refinada após retorno do professor |
| 5 e 6 | Revisão | Levantamento bibliográfico e referencial teórico |
| 7 | Metodologia | Protocolo metodológico e registro das hipóteses |
| 8 a 10 | Dados | Coleta, construção da base e controle de qualidade |
| 11 | Dados | Base congelada e validada |
| 12 e 13 | Análise | Descritiva, Kaplan-Meier e modelo multivariado |
| 14 | Análise | Testes de robustez e consolidação de resultados |
| 15 | Resultados | Redação do artigo e discussão das hipóteses |
| 16 | Apresentação | Apresentação final e publicação de código e base |

O caminho crítico está entre as semanas 8 e 11. Caso a coleta histórica não se confirme, o recuo previsto é concentrar o trabalho no desfecho co-primário de atendimento por país, que depende de uma única fonte e possui a série mais densa. Essa decisão será tomada na semana 10.

---

## 8. Referências

SANTOS, C. M. C.; PIMENTA, C. A. M.; NOBRE, M. R. C. A estratégia PICO para a construção da pergunta de pesquisa e busca de evidências. **Revista Latino-Americana de Enfermagem**, v. 15, n. 3, maio-jun. 2007.

BERGIN, S. M.; WRAIGHT, P. Silver based wound dressings and topical agents for treating diabetic foot ulcers. **Cochrane Database of Systematic Reviews**, n. 1, CD005082, 2006.

KITCHENHAM, B.; CHARTERS, S. **Guidelines for performing Systematic Literature Reviews in Software Engineering**. Technical Report EBSE-2007-01, 2007.

GOMES, R. R. **Projeto em Ciência de Dados IV: da curiosidade à pergunta investigável**. PUC Minas, 2º semestre de 2026.

As fontes de dados primárias estão relacionadas na seção 1.7.
