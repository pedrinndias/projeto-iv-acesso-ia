# Variação regional no piloto Claude × Bedrock

26/11/2026. Análise descritiva dos [145 pares do piloto](../../../dados/intermediario/piloto_eventos.csv),
com 29 regiões fora dos EUA e a definição A (acesso a partir da região por In-Region,
Geo ou Global, incluindo Legacy). A censura usa a última negativa explícita em
20/04/2026. A unidade é modelo × região, numa única plataforma.

| Recorte | Pares | Chegadas | Censuras | Regiões com alguma chegada | Datas exatas | Largura mediana / P90 (dias) | Atraso observado mediano (mín–máx, dias) | Chegadas que compartilham `U` no mesmo modelo | Comparações com ordem definida |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Completo | 145 | 86 | 59 | 29/29 | 11 | 14 / 37 | 6 (0–166) | 82/86 | 232/935 (24,8%) |
| Sem Sonnet 4.5 e 4.6 | 87 | 28 | 59 | 13/29 | 8 | 12 / 119 | 85 (44–146) | 26/28 | 61/123 (49,6%) |
| Sem a coorte de 2024 | 87 | 70 | 17 | 29/29 | 8 | 12 / 26 | 6 (0–166) | 67/70 | 210/878 (23,9%) |

O atraso é a diferença entre lançamento e chegada. A tabela usa a data exata quando
disponível e o ponto médio registrado no CSV nos demais eventos. Os censurados
entram nas contagens. A mediana e a amplitude de atrasos resumem apenas as chegadas
observadas. A largura do intervalo mede a precisão da data, com largura zero para
datas exatas. O P90 usa a mesma regra da [tabela de precisão](../../../resultados/tabelas/piloto_precisao.md).

`U` é a primeira captura positiva. Regiões que compartilham `U` podem ter recebido o
modelo em datas diferentes. Para medir a variação sem assumir que o ponto médio é a
data real, comparei todas as combinações de duas regiões com chegada no mesmo modelo.
A ordem é definida quando a última data possível de uma chegada é anterior à primeira
data possível da outra. Em datas inteiras, `(L, U]` vai de `L+1` a `U`. Datas exatas
são representadas por um único dia. As comparações são descritivas, com dependência
entre pares que compartilham regiões. Os 10 conflitos originais foram preservados,
com 1 no recorte sem 4.5/4.6 e 9 no recorte sem 2024.

| Modelo | Chegadas / 29 | Maior grupo na mesma primeira captura | Comparações com ordem definida | Diferença mínima sustentada entre a primeira e a última chegada observadas |
|---|---:|---|---:|---:|
| Claude 3.5 Sonnet | 9 | 4 em 23/11/2024 | 18/36 | 90 dias |
| Claude 3.5 Sonnet v2 | 7 | 6 em 03/03/2025 | 4/21 | 1 dia |
| Claude 3.7 Sonnet | 12 | 7 em 26/05/2025 | 39/66 | 72 dias |
| Claude Sonnet 4.5 | 29 | 19 em 30/09/2025 | 143/406 | 164 dias |
| Claude Sonnet 4.6 | 29 | 28 em 02/03/2026 | 28/406 | 17 dias |

A diferença mínima é `máx(0, maior data inicial possível − menor data final possível)`
para cada modelo. As contagens dessas comparações permanecem iguais se as datas exatas
forem devolvidas aos intervalos de captura originais.

## O que os recortes mostram

- **Os modelos 4.5 e 4.6 concentram 58 das 86 chegadas.** Os dois maiores grupos por
  primeira captura respondem por 47 chegadas. Sem esses modelos, a mediana descritiva
  vai de 6 para 85 dias e os eventos abrangem 13 regiões. A ordem ainda é distinguível
  em 61 de 123 comparações, com contribuição importante do 3.7. Há variação regional
  detectável, com cobertura baixa nesse recorte.
- **Sem 2024, a cauda da imprecisão diminui.** O P90 da largura cai de 37 para 26 dias.
  A mediana descritiva de 6 dias permanece e 67 de 70 chegadas compartilham `U` com
  outra região do mesmo modelo. A baixa cobertura histórica de 2024 e a concentração
  de capturas positivas dos modelos recentes são questões distintas.
- **Entrada tardia.** Tailândia e México abriram em janeiro de 2025 segundo o panorama
  do projeto. Isso desloca o início do acompanhamento para quatro pares censurados
  dos dois modelos de 2024. Com precisão mensal, o acompanhamento possível da abertura
  a 20/04/2026 fica em 444–474 dias. Esses quatro pares aparecem no recorte completo e
  no recorte sem 4.5/4.6. A operação na estreia foi documentada em 14 dos 59 censurados.
  Para os outros 41, ela fica a confirmar. O inventário de abertura precisa cobrir
  também os pares com chegada. Os recortes preservam os limites calendários, sem
  atribuir um dia de abertura por convenção ou estimar tempos em risco para todos os
  pares. [Auditoria de abertura e censura](../../../docs/piloto/ESTADO.md#auditoria-de-25112026).

## Proposta para a decisão do grupo

1. **Manter a pergunta regional como eixo descritivo, restrito ao Bedrock nesta fase.**
   Pergunta proposta: qual a variação do tempo entre o lançamento de um modelo Claude
   e o primeiro acesso documentado a partir de cada região do Bedrock fora dos EUA?
   Manter a pergunta de atendimento por país como co-primária, com unidade provedor ×
   país e sua própria auditoria de cobertura. A lista de países e o acesso a partir de
   uma região de nuvem medem dimensões diferentes.
2. **Condicionar a análise de associações à cobertura do tempo em risco.** Confirmar
   aberturas das regiões e explicitar o papel da disponibilidade do Bedrock na regra
   de entrada. Se a cobertura permitir, estimar curvas com Turnbull em uma implementação
   que trate censura intervalar e entrada tardia. Avaliar Cox intervalar depois de
   conferir a quantidade de eventos informativos dentro de cada modelo, a dependência
   entre regiões e diferenças de cobertura. O piloto sustenta a análise descritiva
   e ainda não fundamenta um modelo explicativo amplo ou conclusões causais.
3. **Testar Vertex como extensão de viabilidade, depois de fechar Bedrock.** Usar um
   modelo comum e um pequeno conjunto de regiões comparáveis em que a documentação
   distinga origem, processamento e modalidades. A série local tem 43 dias de captura
   até junho de 2026 (44 incluindo julho). Medir a precisão efetiva e a proporção de
   pares sem informação pelo mesmo critério do piloto antes de ampliar o escopo.
   [Cobertura por trimestre](../../../dados/intermediario/cobertura_wayback_2026-08-28.csv).
4. **Reconsiderar Foundry se o histórico reconstruir o desfecho.** A consulta local
   encontrou 161 commits na cadeia de renomeações entre março de 2025 e fevereiro de
   2026. Validar se eles registram mudanças de modelo × região × modalidade, em datas
   úteis, e se o resultado concorda com um anúncio oficial ao menos em uma amostra.
   [Histórico versionado](../../../dados/intermediario/historico_repo_microsoft_2026-09-20.csv).

Esta é a versão para deliberação. Uma vez registrado o escopo do grupo, alinhar a
pergunta e a unidade da Ficha, as regras de observação e entrada no escopo e o método
de análise. A Ficha entregue permanece como registro da versão original.
