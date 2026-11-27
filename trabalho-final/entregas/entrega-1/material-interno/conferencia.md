# Conferência da Entrega 1

**Registro interno da versão assistida anterior.** O template oficial exige redação humana da pergunta e da revisão e elaboração das referências pelo grupo. A auditoria e a base editável estão no [índice da entrega](../README.md).

Verificação de 26/11/2026. Este registro acompanha a minuta local e documenta a seleção e as conferências feitas com assistência de IA.

## Busca e seleção

As nove consultas novas do Apêndice A foram executadas nas duas bases. No OpenAlex, os totais vêm de `meta.count`. Foram examinados até 15 registros devolvidos por consulta. Na SBC OpenLib, conferiu-se o total que a página exibe. A consulta “Claude Bedrock” exibiu “Nenhum resultado encontrado”. Esses números representam resultados brutos por consulta e podem incluir obras repetidas. O registro de 17/09 é histórico, conforme o log do Exercício 2.

- OpenAlex, em ordem das consultas do PDF: 1.196, 7.331, 23, 10.541, 113 e 10. As buscas sobre plataformas, funções sob demanda, RTTs e desigualdade na borda recuperaram Patel et al., Ekwe-Ekwe e Amos, Dang et al. e Martin e Dogar, respectivamente. Os resultados sobre latência servem para caracterizar conectividade. Os estudos que não mediam acesso geográfico nem oferta foram descartados na triagem.
- SBC OpenLib, em ordem: 0, 1 e 5. O retorno único de orquestração data de 2017. Os cinco resultados sobre modelos fundacionais tratavam de avaliação ou aplicação. [Busca direta por Claude Bedrock](https://sol.sbc.org.br/busca/index.php/integrada/results?query=Claude%20Bedrock)
- Dos Exercícios 1 e 3 recuperaram-se Ahmed e Wahed, Amos et al., Knez e McElheran et al. O log do Exercício 1 conserva as consultas sobre `compute divide`, `Internet Archive`, difusão e `AI divide`, e o Exercício 3 conserva três textos integrais. Os materiais de exercícios anteriores serviram de insumo à nova triagem. A seleção final tem oito obras únicas, com seis em veículos revisados por pares e dois preprints.

## Referências e passagem de fidelidade às fontes

Os oito testes em `doi.org` retornaram HTTP 302 para o destino correspondente. A conferência cruzou o DOI, o texto integral e os metadados do editor, da agência registradora ou do repositório acadêmico ligado à publicação. A ordem de autores de Ekwe-Ekwe e Amos segue o registro publicado, corroborado pelo repositório da universidade. O manuscrito aberto exibe a ordem inversa. Para Martin e Dogar, o manuscrito no arXiv tem título anterior e a referência segue o título do periódico. Os localizadores da matriz para Martin e Dogar correspondem à versão aberta consultada.

| Obra | Tipo e localização do achado | Texto integral e DOI |
|---|---|---|
| Ahmed e Wahed (2020) | Preprint. Resumo, estimação por controle sintético e seção *Limitations*. O estudo conta publicações e instituições. | [Texto](https://arxiv.org/pdf/2010.15581) · [DOI](https://doi.org/10.48550/arXiv.2010.15581) |
| Amos et al. (2021) | ACM WWW. Seções 4 e 5, figura 1 e tabela 1. A tabela documenta motivos das perdas de coleta. | [Texto](https://arxiv.org/pdf/2008.09159) · [DOI](https://doi.org/10.1145/3442381.3450048) |
| Dang et al. (2021) | ACM IMC. Seções 3 a 5. Compara a latência e a escolha da plataforma de medição. | [Texto](https://cloudreachability.github.io/documents/cloudy-imc-2021.pdf) · [DOI](https://doi.org/10.1145/3487552.3487854) |
| Ekwe-Ekwe e Amos (2024) | IEEE CLOUD. Seções II, III-E e VI. Inventário de serviços de funções e de sua cobertura. | [Texto e registro institucional](https://research-repository.st-andrews.ac.uk/handle/10023/30446) · [DOI](https://doi.org/10.1109/CLOUD62652.2024.00055) |
| Knez (2023) | *Journal of Evolutionary Economics*. Resumo e seções 4 e 5. Foram usadas 36 tecnologias na avaliação empírica. A aproximação agrega tecnologias e países. | PDF do Exercício 3 · [DOI](https://doi.org/10.1007/s00191-023-00830-w) |
| Martin e Dogar (2023) | *Proceedings of the ACM on Networking*, CoNEXT3. Resumo e seções 3 a 5 da versão aberta. O desfecho é latência. | [Texto](https://arxiv.org/pdf/2304.05481) · [DOI](https://doi.org/10.1145/3629138) |
| McElheran et al. (2024) | *Journal of Economics & Management Strategy*. Seções 3.1, 3.3 e 6. O percentual de 5,8% refere-se ao uso reportado no recorte de 2017. | PDF do Exercício 3 · [DOI](https://doi.org/10.1111/jems.12576) |
| Patel et al. (2024) | Preprint. Seções 3.2.1 e 4.6, tabela 11. O quadro compara serviços acessíveis por API em nível de plataforma. | [Texto](https://arxiv.org/pdf/2412.06044) · [DOI](https://doi.org/10.48550/arXiv.2412.06044) |

A conferência do CSV do piloto encontrou cinco modelos, 29 regiões, 145 pares, 86 eventos com limite superior e 59 censuras à direita. As 59 censuras têm limite inferior em 20/04/2026. O marco inicial adotado é o anúncio oficial do modelo, conforme o veredito. A data de 30/06/2026 refere-se ao fim da janela. A regra de origem da chamada segue a definição A do piloto. [Documentação do Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html)

## Passagem de argumentação e rubrica

| Critério | Conferência |
|---|---|
| Problema (6 pontos) | A pergunta admite resultados diferentes, como intervalos predominantemente sobrepostos ou regiões com ordem de chegada distinguível. Há três objetivos verificáveis e três itens explícitos de delimitação. A justificativa ocupa quatro linhas no PDF. A ratificação do recorte descritivo pelo grupo está pendente. |
| Protocolo e seleção (4 pontos) | Duas bases consultadas, com data, expressão, campos, filtros e totais. Oito obras, seis revisadas por pares e dois preprints identificados. |
| Matriz (3 pontos) | Oito linhas e oito colunas, com indicação de campos sem informação e localizadores. As iniciais aguardam o preenchimento humano. |
| Revisão (5 pontos) | Seis afirmações em duas páginas, com leitura de progressão sem as fontes. Os parágrafos vão de conectividade e oferta à datação histórica. A lacuna fica delimitada ao corpus e leva à pergunta regional. |
| Formato e referências (2 pontos) | PDF compilado em Tectonic, bibliografia produzida com BibTeX, oito DOIs testados e apêndices A, B e C presentes. O link público da entrega está pendente e deverá ser testado sem login. |

## Pendências do grupo

Confirmar a composição vigente, pois a Ficha entregue documenta Pedro Dias Soares e Eduardo Velloso Landeiro e o enunciado prevê três integrantes. Ratificar o recorte que usa Claude no Bedrock como pergunta principal desta entrega. O atendimento por país mantém-se como proposta de pergunta co-primária, com unidade própria país × provedor e auditoria de cobertura independente. Completar as leituras, a redação e as duas conferências humanas, e registrar as atribuições efetivas na matriz e no Apêndice C. Inserir o link público do projeto LaTeX na capa e validar o acesso sem login.

Para recompilar, execute `tectonic entrega-1.tex` nesta pasta. Para editar o link de capa, atualize a macro `\linkprojeto` no fonte LaTeX.
