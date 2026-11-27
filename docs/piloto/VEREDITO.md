# Veredito do piloto do desfecho

03/10/2026 · 5 modelos Claude × 29 regiões do Amazon Bedrock fora dos EUA · base:
`resultados/tabelas/piloto_precisao.md` e `docs/piloto/ESTADO.md`. **Recomendação; a
decisão é do grupo.**

## Resultado

**O piloto passa no critério registrado antes da coleta.** A data de chegada de um
modelo a uma região foi determinada com **incerteza mediana de 14 dias** (limiar: 30),
P90 de 37 dias, e nenhum par truncado à esquerda no cálculo do piloto. Dos 145 pares,
86 tiveram chegada documentada e 59 foram censurados à direita em **20/04/2026**,
data da última observação negativa explícita de cada par. As capturas posteriores até
30/06/2026 omitem essas regiões das tabelas dos respectivos modelos e deixam em aberto
eventuais mudanças no intervalo. Ver a [auditoria no estado do piloto](ESTADO.md#auditoria-de-25112026).

O resultado vale para a **definição A**, escolhida pelo grupo antes da etapa 4:
disponível = acessível a partir da região de qualquer forma, com Legacy contando. Com a
definição original (só inferência local), o piloto falharia por construção: a página
antiga da AWS não distingue local de roteado (94% dos seus `Yes` aparecem como
Geo/Global na página nova), e a série In-Region só começa em 11/03/2026.

## Recomendação

**Manter a pergunta regional como principal, com o Bedrock como espinha dorsal**, e a
pergunta de países como co-primária. Três condições:

1. **Documentar as origens do Sonnet 4.5.** A auditoria de 25/11/2026 encontrou
   correspondência exata entre os 23 `Yes` de 30/09 e as 23 origens do perfil Global
   em 04/10/2025, e entre os 27 `Yes` de 20/11 e as 27 origens em 25/11/2025. As
   capturas sustentam a leitura de origem nas datas comparadas e corroboram os limites
   registrados, com uma defasagem de alguns dias entre as fontes. O total de 10
   divergências entre documentação e anúncios, oito do Sonnet 4.5, permanece no CSV
   como trilha de auditoria. A variação regional resultante ainda precisa ser medida.
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
- **Riscos (§6):** documentar o alcance da validação do `Yes` para Sonnet 4.5, a
  precisão desigual entre coortes e a entrada tardia de regiões abertas após a estreia.

**Próximo passo:** medir a variação regional com a entrada tardia onde houver evidência,
comparando a base completa com os recortes sem Sonnet 4.5/4.6 e sem a coorte de 2024.
