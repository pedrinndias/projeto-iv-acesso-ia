# Conceitos de método para a leitura dos três artigos

Uso permitido pelo enunciado (§6: "esclarecer um conceito técnico"). Este texto explica os
métodos **em geral**, e não o que cada artigo fez ou concluiu. O tipo de estudo de cada artigo
vem da tabela do Exercício 1, que foi montada a partir dos resumos. Como o método foi aplicado,
e se foi bem aplicado, é a leitura de vocês que diz. Não citar este arquivo no fichamento.

## Para os três: como ler um resultado estatístico

- **Coeficiente:** quanto o desfecho muda, em média, quando a variável muda uma unidade,
  mantidas as demais constantes.
- **Erro-padrão e intervalo de confiança:** são a "medida de dispersão" que a apostila pede. Um
  coeficiente sem erro-padrão ou intervalo é um resultado incompleto. Estrelas (\*, \*\*, \*\*\*)
  indicam significância, e não tamanho do efeito.
- **Efeitos fixos:** controlam diferenças estáveis entre unidades (país, firma, instituição) ou
  entre períodos.
- **Robustez:** repetir a estimativa com outras especificações, amostras ou definições. É o
  equivalente, em estudo observacional, da ablação de ML.
- **Associação × causa:** dado observacional mostra associação. Para falar em efeito, o artigo
  precisa de um desenho que crie um contrafactual crível. Se a conclusão usar verbo causal sem
  esse desenho, é o padrão "conclusão mais ampla que o experimento".

## Controle sintético generalizado (Ahmed e Wahed, 2020, segundo o Ex1)

- **Controle sintético clássico:** há uma unidade tratada. Constrói-se um "gêmeo" como média
  ponderada de unidades não tratadas que reproduz a trajetória da tratada **antes** do
  tratamento. O efeito estimado é a distância entre as duas trajetórias **depois** dele.
- **Versão generalizada** (associada a Xu, 2017; conferir antes de citar): admite várias unidades
  tratadas, inclusive em momentos diferentes. Estima um modelo de fatores latentes com as não
  tratadas e prevê o contrafactual de cada tratada.
- **O que conferir:**
  - o que foi definido como "tratamento" e em que data;
  - se o ajuste antes do tratamento é bom (as curvas coincidem?);
  - como foi escolhido o número de fatores;
  - se há intervalo de confiança e teste placebo.
- **Na auditoria:** a figura central costuma ser "tratada × sintética" ao longo do tempo. Vejam
  se há faixa de incerteza e se o eixo está truncado.

## Análise descritiva sobre levantamento de firmas (McElheran et al., 2024, segundo o Ex1)

- **Levantamento do Census Bureau:** respostas de questionário de uma amostra muito grande de
  firmas. **Pesos amostrais** fazem a amostra representar a população.
- **O que conferir:**
  - como "uso de IA" foi definido e perguntado (autodeclaração, que tecnologias contam);
  - o período de referência dos dados;
  - a taxa de resposta;
  - se a unidade é a firma ou o estabelecimento;
  - se os percentuais são ponderados.
- **Desenho:** estudo descritivo de corte transversal. Mostra **quem** e **onde**, e não
  **por quê**.
- **Na auditoria:** mapas e gráficos de participação percentual. Há intervalo de confiança? A
  escala da cor ou do eixo exagera diferenças?

## Modelo de difusão calibrado (Knez, 2023, segundo o Ex1)

- **Modelos de difusão entre países:** costumam separar duas coisas. Uma é **quando** a
  tecnologia chega (a defasagem de adoção). A outra é **com que intensidade** ela passa a ser
  usada depois.
- **Calibrar** é escolher os parâmetros para que o modelo reproduza dados observados. Às vezes
  isso é feito por mínimos quadrados não lineares.
- **Bases:**
  - CHAT (*Cross-country Historical Adoption of Technology*): adoção histórica de tecnologias
    por país;
  - Penn World Table: renda, capital e produtividade por país.
- **O que conferir:**
  - o que é **premissa** do modelo e o que é **resultado**. Num modelo calibrado, o resultado
    vale condicionado às premissas;
  - quais alvos foram usados na calibração;
  - se o modelo foi testado em dados que não serviram de alvo;
  - se há análise de sensibilidade.
- **Na auditoria:** "quantas execuções" vira quantos países e tecnologias entram. "Dispersão"
  vira o intervalo dos parâmetros estimados ou a dispersão do ajuste entre países.

## Reserva: análise de classes latentes (Wang et al., 2024)

- Agrupa respondentes em perfis não observados a partir do padrão das respostas.
- **O que conferir:** como foi escolhido o número de classes (BIC, entropia), o tamanho de cada
  classe e se os rótulos dados às classes são interpretação dos autores.
