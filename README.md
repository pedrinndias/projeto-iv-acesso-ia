# Desigualdade geográfica no acesso a modelos de IA generativa comercial

Projeto de pesquisa da disciplina **Projeto em Ciência de Dados IV** — PUC Minas, 2º semestre de 2026.
Curso de Ciência de Dados & Inteligência Artificial. Prof. Rodrigo Richard Gomes.

**Integrantes:** Pedro Dias Soares · Eduardo Velloso Landeiro

---

## Pergunta de pesquisa

> Quais fatores estão associados à defasagem de disponibilidade regional de modelos de IA
> generativa comercial de provedores estadunidenses (Anthropic, OpenAI e Google), nas
> plataformas AWS Bedrock, Google Vertex AI e Microsoft Foundry, entre abril de 2024 e
> junho de 2026?

**Pergunta co-primária**

> Quais características dos países estão associadas à sua ausência das listas oficiais de
> atendimento dos provedores de IA estadunidenses, e como essa composição mudou entre
> maio de 2023 e junho de 2026?

O documento completo está em [`docs/Ficha-Inicial-Projeto-IV.md`](docs/Ficha-Inicial-Projeto-IV.md).

## Situação atual

O [trabalho final](trabalho-final/) reúne as [demandas da disciplina](trabalho-final/demandas/README.md) e as [entregas produzidas](trabalho-final/entregas/README.md), incluindo a preparação da Entrega 1 e a análise de variação regional do piloto.

**Para continuar o trabalho, comece pela [passagem de 27/11/2026](trabalho-final/PASSAGEM.md)**, que aponta a [auditoria da Entrega 1](trabalho-final/auditoria/2026-11-27-auditoria-entrega-1.pdf) e as decisões pendentes.

| Etapa | Situação |
|---|---|
| Tema | Concluída |
| Problema | Concluída |
| Pergunta | Concluída — sujeita a refinamento após retorno do professor |
| Objetivos | Rascunho |
| Revisão bibliográfica | Em andamento — 10 trabalhos levantados e verificados no Exercício 1; leitura integral pendente |
| Metodologia | Rascunho |
| Coleta de dados | Viabilidade das fontes verificada (seção 3 da Ficha); coleta principal não iniciada |
| Análise | Não iniciada |
| Resultados | Não iniciada |
| Apresentação | Não iniciada |

## Estrutura do repositório

```
docs/          Documentos do projeto
  entregas/    Versões efetivamente entregues ao professor, com data no nome
  versoes/     Rascunhos e versões anteriores, para histórico
referencias/   Bibliografia em PDF e fichamento
dados/
  bruto/       Dados como vieram da fonte. NUNCA editar à mão.
  intermediario/ Dados tratados, prontos para análise
  final/       Base consolidada usada nos resultados
src/
  coleta/      Scripts que baixam dados das fontes
  tratamento/  Scripts de limpeza e consolidação
  analise/     Scripts de análise estatística
notebooks/     Exploração. Código que virar definitivo migra para src/
resultados/    Figuras e tabelas geradas
```

## Como rodar

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python src/coleta/servicos_por_regiao_aws.py     # variável de controle de maturidade
python src/coleta/cobertura_wayback.py           # cobertura histórica das fontes
python src/coleta/historico_repo_microsoft.py    # histórico do repositório da Microsoft
```

Os scripts não têm dependência externa: usam apenas a biblioteca padrão. O passo do
`pip install` só será necessário quando os scripts de análise entrarem.

## Combinados do grupo

1. **`dados/bruto/` é imutável.** Se um dado precisa ser corrigido, o script de tratamento
   corrige e grava em `dados/intermediario/`. O bruto fica como veio da fonte.
2. **Todo dado coletado guarda a data da coleta e a URL de origem.** Sem isso o resultado
   não é reprodutível e a defasagem medida não pode ser auditada.
3. **Trabalhar em branch e abrir pull request.** A `main` fica sempre em estado entregável.
4. **Não commitar arquivo de dados com mais de 50 MB.** Se acontecer, avisar o grupo antes.
5. **O que for entregue ao professor vai para `docs/entregas/` com a data no nome do arquivo**,
   e não é editado depois. Alterações viram uma nova versão.

## Referências

- SANTOS, C. M. C.; PIMENTA, C. A. M.; NOBRE, M. R. C. A estratégia PICO para a construção da
  pergunta de pesquisa e busca de evidências. *Rev. Latino-Am. Enfermagem*, v. 15, n. 3, 2007.
- KITCHENHAM, B.; CHARTERS, S. *Guidelines for performing Systematic Literature Reviews in
  Software Engineering*. Technical Report EBSE-2007-01, 2007.

Fontes de dados primárias: ver seção 1.7 da Ficha Inicial.
