# Piloto do desfecho: precisão da data de chegada

Gerado por `src/tratamento/piloto_intervalos.py`. Regiões fora dos EUA, 5 modelos Claude no
Amazon Bedrock, definição do grupo: acessível de qualquer forma, Legacy conta.
Largura = dias do intervalo (L, U] em que a chegada aconteceu; 0 quando há data exata.
Defasagem = dias entre o anúncio e o ponto médio do intervalo (ou a data exata).

| Grupo | Pares | Eventos | % data exata | Mediana largura (d) | P90 largura (d) | Mediana só Wayback (d) | Truncados | Censurados | Conflitos | Mediana defasagem (d) |
|---|---|---|---|---|---|---|---|---|---|---|
| **Total** | 145 | 86 | 13% | 14.0 | 37 | 14 | 0 | 59 | 10 | 6.0 |
| Lançados em 2024 | 58 | 16 | 19% | 25.0 | 119 | 25 | 0 | 42 | 1 | 94.0 |
| Lançados em 2025 | 58 | 41 | 15% | 1 | 26 | 1 | 0 | 17 | 8 | 26 |
| Lançados em 2026 | 29 | 29 | 7% | 14 | 14 | 14 | 0 | 0 | 1 | 6 |
| Claude 3.5 Sonnet | 29 | 9 | 33% | 19 | 157 | 28.0 | 0 | 20 | 0 | 77 |
| Claude 3.5 Sonnet v2 | 29 | 7 | 0% | 25 | 119 | 25 | 0 | 22 | 1 | 119 |
| Claude 3.7 Sonnet | 29 | 12 | 42% | 12.0 | 12 | 12 | 0 | 17 | 0 | 85.0 |
| Claude Sonnet 4.5 | 29 | 29 | 3% | 1 | 52 | 1.0 | 0 | 0 | 8 | 0 |
| Claude Sonnet 4.6 | 29 | 29 | 7% | 14 | 14 | 14 | 0 | 0 | 1 | 6 |

Critério registrado antes da coleta: mediana da largura ≤ 30 dias → a pergunta
regional segue; > 30 dias, ou mais da metade dos pares truncados/sem informação → a
pergunta de países vira a principal.
