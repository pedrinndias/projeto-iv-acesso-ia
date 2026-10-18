# Veredito do piloto do desfecho

03/10/2026 · 5 modelos Claude × 29 regiões do Amazon Bedrock fora dos EUA · base:
`resultados/tabelas/piloto_precisao.md` e `docs/piloto/ESTADO.md`. **Recomendação; a
decisão é do grupo.**

## Resultado

**O piloto passa no critério registrado antes da coleta.** A data de chegada de um
modelo a uma região foi determinada com **incerteza mediana de 14 dias** (limiar: 30),
P90 de 37 dias, e nenhum par truncado à esquerda. Dos 145 pares, 86 tiveram chegada
observada e 59 nunca receberam o modelo até 30/06/2026. Esses 59 são censura à direita,
o próprio formato do desfecho, e não falta de dado.

O resultado vale para a **definição A**, escolhida pelo grupo antes da etapa 4:
disponível = acessível a partir da região de qualquer forma, com Legacy contando. Com a
definição original (só inferência local), o piloto falharia por construção: a página
antiga da AWS não distingue local de roteado (94% dos seus `Yes` aparecem como
Geo/Global na página nova), e a série In-Region só começa em 11/03/2026.

## Recomendação

**Manter a pergunta regional como principal, com o Bedrock como espinha dorsal**, e a
pergunta de países como co-primária. Três condições:

1. **Fechar o construto antes da coleta completa (semana 8).** Oito dos 10 conflitos
   são do Sonnet 4.5. A página antiga o mostra acessível no Japão, Austrália, Canadá e
   Bahrein desde o dia 1, mas o blog da AWS anuncia esse acesso semanas ou meses depois.
   Se o `Yes` antigo incluía regiões que só **recebem** tráfego do roteamento global, a
   definição A superestima o acesso dos modelos recentes. **Teste:** baixar do Wayback a
   página de perfis de inferência (`inference-profiles-support.html`) de out–nov/2025 e
   conferir se Japão, Canadá e Bahrein constavam como **regiões de origem** do perfil
   global do Sonnet 4.5. Se constavam, o conflito é só de tipo (o blog anunciou o Geo) e a
   definição A se sustenta. Se não constavam, usar como data de chegada a primeira
   aparição como região de origem.
2. **Tratar a imprecisão de 2024 no método, não escondê-la.** A coorte de 2024 tem
   mediana de 25 dias e P90 de 119 (capturas ralas); a de 2025, mediana de 1 dia.
   Kaplan-Meier e Cox passam a ter as versões para **censura intervalar** (estimador de
   Turnbull; Cox para dados intervalares). Os modelos de 2024 entram na análise principal
   e saem numa análise de sensibilidade.
3. **Não estender a conclusão além do testado.** O piloto cobriu só Claude no Bedrock.
   O Google Vertex tem cerca de 1 captura por mês (precisão esperada bem pior), e OpenAI e
   Microsoft não foram testados. Antes de prometer as três plataformas, repetir a etapa 3
   num modelo do Vertex.

## O que muda na Ficha e no escopo

- **Desfecho (§2.3, PICOC O; escopo §7.3):** "disponível" passa a ser acessível a
  partir da região, por qualquer tipo de inferência, com Legacy contando. Marco zero = data
  do anúncio oficial, usada também como piso do intervalo.
- **Hipótese H1 (§5.2):** com o roteamento global, o acesso se descola da capacidade
  instalada na região. A predição de H1 precisa ser reescrita: o controle por número de
  serviços continua, mas "escassez de hardware local" deixa de ser o mecanismo óbvio.
- **Fontes (§3.1):** a série AWS passa a ser `models-regions.html` até 20/04/2026 mais
  `models-region-compatibility.html` desde 11/03/2026. A página antiga foi esvaziada.
- **Método (§5.3):** versões intervalares de Kaplan-Meier e Cox. A comparação
  "atraso de IA × 13% de defasagem geral" (secundária 4) e o desenho de
  diferenças-em-diferenças continuam inviáveis como estão.
- **Riscos (§6):** acrescentar a ambiguidade do `Yes` antigo (região de origem ou de
  destino) e a precisão desigual entre coortes.

**Próximo passo único:** o teste do item 1, uma etapa curta e de baixo custo, antes de
começar a coleta das semanas 8–10.
