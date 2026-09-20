# Prompt de execução — Exercício 1: Busca e Revisão Bibliográfica Guiada

> Use este arquivo como prompt inicial de uma sessão dedicada. Ele é autocontido:
> não depende do histórico da conversa em que foi escrito.

---

## Contexto

Sou Pedro Dias Soares, aluno de Ciência de Dados e Inteligência Artificial na PUC Minas,
4º semestre, disciplina **Projeto em Ciência de Dados IV** (2º semestre de 2026,
Prof. Rodrigo Richard Gomes).

Esta é uma **atividade individual**, ainda que o projeto da disciplina seja em dupla com
Eduardo Velloso Landeiro. O texto tem que ser autoral e meu.

O repositório do projeto está em
`/Users/pedro/Documents/Faculdade e Estudos/Semestre 4/Projeto IV`.
Antes de qualquer coisa, **leia `docs/Ficha-Inicial-Projeto-IV.md` por inteiro** e
`docs/versoes/escopo-completo-v1.md` nas seções 7.3 (definições operacionais) e
7.4 (estratégia de busca bibliográfica). O exercício se apoia neles.

Resumo do projeto, para orientação: estudo observacional longitudinal que mede a
defasagem, em dias, até modelos de IA generativa comercial (Anthropic, OpenAI, Google)
ficarem disponíveis em cada região de nuvem, entre abr/2024 e jun/2026, e testa quatro
hipóteses concorrentes para explicá-la — infraestrutura, mercado, regulação e
geopolítica. O desfecho é tempo até evento com censura à direita (Kaplan-Meier + Cox).

---

## O que tem que ser entregue

PDF **gerado a partir de LaTeX**, contendo, nesta ordem exata:

1. Título do tema escolhido
2. Introdução breve ao tema
3. Estratégia de busca bibliográfica
4. Lista dos trabalhos selecionados
5. Tabela comparativa
6. Síntese crítica (2 a 4 páginas)
7. Referências bibliográficas

E mais uma seção obrigatória, com **este título literal**: **Link do projeto LaTeX**.

### Critérios de avaliação (são estes os 8 que o professor vai usar)

1. adequação e clareza do tema escolhido
2. qualidade da estratégia de busca
3. relevância dos trabalhos selecionados
4. organização e completude da tabela comparativa
5. capacidade de síntese e análise crítica
6. identificação de lacunas ou possibilidades de pesquisa
7. clareza, coesão e correção da escrita acadêmica
8. entrega do PDF gerado em LaTeX com o respectivo link para o arquivo-fonte

Note que 5 dos 8 critérios são sobre argumentação, não sobre garimpo de artigos.
Distribua o esforço de acordo.

---

## Tema

Trabalhe com este tema, já decidido:

> **Desigualdade geográfica no acesso a serviços de inteligência artificial em nuvem:
> como a literatura mede defasagem de adoção e assimetria de acesso entre países.**

A escolha é deliberada. O tema do projeto em si ("defasagem de disponibilidade regional
de modelos de IA") é emergente demais para render 5–10 trabalhos acadêmicos recentes na
interseção exata — a própria §7.4 do escopo reconhece isso. Este recorte desloca a
revisão para a **camada de medição**, onde existe literatura madura, e mantém o
alinhamento com o projeto.

Enuncie o tema em uma frase clara na seção 1, como o enunciado pede.

### As três correntes a cobrir

A revisão deve atravessar três corpos de literatura, porque é o contraste entre eles que
sustenta a síntese crítica:

- **C1 — Divisão digital e desigualdade digital**, incluindo extensões recentes para IA.
- **C2 — Difusão de tecnologia e defasagem de adoção entre países**, onde "adoption lag"
  é construto medido. É a corrente que ancora o desfecho primário do projeto.
- **C3 — Governança de computação, soberania digital, residência de dados e controles
  de exportação aplicados a IA.**

Meta de composição: pelo menos 2 trabalhos por corrente, total entre 7 e 9.
(O mínimo do enunciado é 5 e o máximo é 10; 7–9 dá margem sem inflar.)

---

## Etapa 1 — Estratégia de busca

Bases a consultar, nesta ordem: **Scopus, Web of Science, ACM Digital Library,
IEEE Xplore, arXiv (cs.CY, econ.GN), SSRN, SciELO e BDTD.**
Google Scholar serve para rastrear citações e achar a versão publicada, **não** como
base primária de busca.

Monte as strings por componente, com `OR` dentro do componente e `AND` entre
componentes, seguindo Santos et al. (2007). Parta das strings da §7.4 do escopo e
adapte-as ao recorte deste exercício — elas foram escritas para o projeto inteiro e
aqui o alvo é a literatura de medição.

Declare explicitamente, na seção 3 do texto, duas coisas que valem ponto no critério 2:

- **Vocabulário controlado.** MeSH/DeCS são da saúde e não se aplicam. Os equivalentes
  em Computação são o **ACM Computing Classification System** e o **IEEE Thesaurus**.
  Diga isso.
- **O componente C do PICO.** Em revisão exploratória sobre tema emergente, incluir a
  comparação na string derruba a recuperação. Deixe C implícito na busca e explícito no
  desenho — e **declare** que fez isso, em vez de omitir.

Filtros: 2019–2026; artigos, atas de conferência, preprints e teses.

### Registro obrigatório da busca

Grave um log em CSV na pasta do exercício, com uma linha por base consultada:

```
base,data_busca,string_exata,n_retornos,n_apos_titulo_resumo,n_apos_leitura_integral,observacoes
```

Esse log é o que separa uma revisão sistemática de uma narrativa, e Santos et al. são
explícitos ao criticar revisões narrativas por serem tendenciosas e inconclusivas.
Resuma-o como tabela na seção 3 do PDF.

### Contingência — regra de decisão, não improviso

Se depois de rodar as strings primárias em todas as bases o conjunto elegível tiver
**menos de 7 trabalhos**, aplique a escada nesta ordem, parando assim que chegar a 7,
e **registre no log qual degrau foi usado**:

1. Retire o componente de desfecho (O) da string, mantendo P AND E.
2. Aceite relatórios técnicos de instituições reconhecidas (OCDE, Banco Mundial, UIT,
   AI Now, institutos de pesquisa universitários) como fonte acadêmica — declarando o
   critério no texto.
3. Faça busca por citação (backward/forward) a partir dos trabalhos já selecionados.
4. Amplie a janela para 2015–2026, mantendo a maioria em ≤5 anos.

Nunca resolva falta de resultado inventando trabalho.

---

## Etapa 2 — Seleção

Critérios de inclusão:
- acadêmico (periódico, conferência, repositório científico reconhecido ou tese);
- diretamente relacionado ao tema;
- **a maioria com no máximo 5 anos** — hoje é setembro de 2026, logo o corte é **2021**.
  Conte explicitamente quantos estão dentro e fora, e reporte o número. Clássicos de
  difusão de tecnologia são bem-vindos, mas em minoria.

Critérios de exclusão, para declarar no texto: trabalhos puramente técnicos sobre
arquitetura de rede, aprendizado federado ou computação de borda, que aparecem nas
strings mas não tratam de assimetria de acesso.

### Portão rígido de verificação — não negociável

**Nenhuma referência entra no `.bib` sem ter sido verificada como existente.**
Para cada trabalho, confirme e anote: DOI resolvido, ou URL estável efetivamente
aberta (arXiv, SSRN, biblioteca digital, repositório institucional). Confira que
autores, ano, título e veículo batem com a fonte.

Se não conseguir verificar, **descarte o trabalho e diga que descartou**. Citação
inventada em entrega acadêmica é problema de integridade, não erro de digitação.

Ao final, apresente a lista de verificação: para cada referência, o DOI ou URL conferido.

---

## Etapa 3 — Tabela comparativa

Colunas mínimas exigidas pelo enunciado, todas obrigatórias:

Autor(es)/Ano · Título · Problema investigado · Método ou abordagem · **Base de dados
utilizada** · Principais resultados · Limitações observadas

**Regra para a coluna "Base de dados utilizada"** — é o *dataset do estudo*, não a base
bibliográfica onde você achou o artigo. Boa parte da literatura de C3 é teórica ou
jurídica e não usa dataset. Nesses casos, em vez de travessão, escreva a natureza do
material: `corpus normativo`, `estudo conceitual, sem dados primários`,
`survey com N=...`, `painel de países, fonte X`. Uma coluna cheia de `—` é lida como
tabela incompleta e custa ponto no critério 4.

**Nota de formatação.** Sete colunas não cabem em página retrato. Use `landscape` do
pacote `pdflscape` para a página da tabela, `tabularx` com `\small` ou `\footnotesize`,
e `booktabs` para as réguas. Se ainda assim estourar, quebre em duas tabelas
(identificação + análise) mantendo todas as sete colunas presentes.

---

## Etapa 4 — Síntese crítica (2 a 4 páginas)

Cinco movimentos obrigatórios, todos cobrados no enunciado:

1. **O que os trabalhos têm em comum.** Não liste um a um — isso é resumo, não síntese.
   Identifique o pressuposto compartilhado: todos tratam acesso desigual a tecnologia
   como fenômeno mensurável, e quase todos medem na camada de conectividade ou de
   adoção de dispositivo.
2. **Diferenças entre abordagens.** Organize por eixo, não por artigo:
   unidade de análise (indivíduo / país / firma), fonte de dado (survey / painel
   macro / telemetria / documento), e método (descritivo / econométrico / qualitativo).
3. **Tendências.** O deslocamento do objeto — de acesso à internet, para qualidade de
   uso, e agora para acesso à capacidade computacional de fronteira.
4. **Lacunas.** É aqui que o exercício encontra o projeto. Argumente, com base no que a
   tabela mostra: ninguém mede assimetria de acesso **na camada de computação de IA**,
   nem usa **documentação oficial arquivada** como série temporal, nem separa atraso
   específico de IA do atraso geral de infraestrutura da região.
5. **Investigação futura.** Descreva o desenho do projeto como resposta à lacuna —
   defasagem em dias como desfecho, censura à direita, controle por maturidade da
   região. Em terceira pessoa, como proposta de pesquisa, **sem** dizer "meu projeto".

Escreva em português acadêmico, voz impessoal, sem adjetivo de entusiasmo. Toda
afirmação sobre um trabalho tem que ser rastreável à linha dele na tabela.

---

## Etapa 5 — LaTeX e ABNT

Plataforma: **Overleaf**. Ao final, gere o link de compartilhamento e configure-o como
**"Anyone with this link can view"** — link não compartilhado invalida o critério 8.
Coloque-o na seção **Link do projeto LaTeX**, visível no PDF.

Esqueleto mínimo:

```latex
\documentclass[12pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[brazil]{babel}
\usepackage{booktabs,tabularx,pdflscape,geometry,hyperref}
\usepackage[backend=biber,style=abnt]{biblatex}
\addbibresource{referencias.bib}
\begin{document}
% ... seções 1 a 6 ...
\printbibliography[title={Referências}]
\end{document}
```

Armadilhas de compilação, verifique cada uma:
- o estilo `abnt` vem do pacote **biblatex-abnt** e exige **backend=biber**. Compilar com
  bibtex não funciona. No Overleaf: Menu → Compiler → pdfLaTeX, e biber é automático,
  mas confirme no log.
- `\addbibresource{referencias.bib}` leva a extensão `.bib` junto.
- preprints do arXiv entram como `@online` ou `@misc` com `eprint` e
  `eprinttype={arxiv}`, não como `@article`.
- compile **duas vezes** depois de rodar o biber, senão as citações saem como `[?]`.

Antes de exportar, confira no PDF: nenhuma citação como `[?]`, nenhuma referência órfã
na lista, e todas as entradas do `.bib` efetivamente citadas no texto.

---

## Restrições

- **Texto autoral.** O enunciado é explícito: cópia de resumo automático ou trecho
  literal sem citação adequada não é aceita. Paráfrase sempre, citação direta só quando
  a formulação exata importar, entre aspas e com página.
- **Nada de referência não verificada**, conforme o portão da Etapa 2.
- Não invente resultado, número ou limitação de um trabalho. Se não conseguiu ler o
  texto completo, diga na coluna de limitações que a leitura foi do resumo e da
  introdução.

---

## Artefatos a produzir

Na pasta `Exercícios/Exercício 1 – Busca e Revisão Bibliográfica Guiada/`:

| Arquivo | Conteúdo |
|---|---|
| `log-busca.csv` | registro base a base, conforme Etapa 1 |
| `referencias.bib` | entradas verificadas, com DOI ou URL |
| `revisao.tex` | fonte LaTeX |
| `revisao.pdf` | PDF compilado, o que vai ser entregue |
| `verificacao-referencias.md` | lista referência → DOI/URL conferido |

A pasta `Exercícios/` ainda está fora do controle de versão (`git status` mostra
`?? Exercícios/`). Decida comigo se entra no repo antes de commitar — os PDFs de
terceiros têm a mesma questão de direitos autorais já anotada em
`referencias/README.md`.

---

## Ordem de execução e pontos de parada

Pare e me mostre o resultado ao fim de **cada** etapa. Não encadeie do tema até o PDF
sem passar por mim.

1. Ler o projeto, confirmar o recorte do tema e as strings → **parar**
2. Rodar as buscas, entregar o log e a lista de candidatos → **parar**
3. Verificar existência de cada referência, entregar a lista de conferência → **parar**
4. Montar a tabela comparativa → **parar**
5. Escrever a síntese crítica → **parar**
6. Montar o LaTeX, compilar e conferir o PDF → **parar**

## Checagem final, mapeada nos 8 critérios

- [ ] tema em uma frase clara, na abertura (crit. 1)
- [ ] bases, palavras-chave, combinações e filtros descritos; vocabulário controlado e
      tratamento do componente C declarados; log em tabela (crit. 2)
- [ ] 7 a 9 trabalhos, maioria ≤ 2021, contagem reportada, todos verificados (crit. 3)
- [ ] tabela com as 7 colunas, sem célula vazia, coluna de base de dados preenchida
      segundo a regra (crit. 4)
- [ ] síntese de 2 a 4 páginas com os 5 movimentos, organizada por eixo e não por
      artigo (crit. 5)
- [ ] lacunas argumentadas a partir da tabela, com proposta de investigação futura
      (crit. 6)
- [ ] português acadêmico impessoal, revisado (crit. 7)
- [ ] PDF saído de LaTeX, referências ABNT via biblatex, seção "Link do projeto LaTeX"
      com link em modo de visualização pública (crit. 8)
