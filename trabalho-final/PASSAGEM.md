# Passagem do trabalho final — 27/11/2026

Ponto de partida para quem continua o projeto. Ao abrir o Claude na raiz do repositório, peça que ele leia este arquivo primeiro.

## Onde estamos

| Etapa | Prazo | Situação em 27/11 |
|---|---|---|
| Entrega 1 — problema e revisão | 30/11/2026 | Base LaTeX pronta e compilando, **sem conteúdo**. Falta redigir, preencher a matriz, cadastrar referências, link de leitura e nota de autoria. |
| Entrega 2 — + metodologia | 07/12/2026 | Só o cronograma. Insumos no [veredito do piloto](../docs/piloto/VEREDITO.md) e na [Ficha](../docs/Ficha-Inicial-Projeto-IV.md). |
| Entrega 3 — integração, conclusão e vídeo | 14/12/2026 | Não iniciada. |

O diagnóstico completo, requisito por requisito, está na [auditoria de 27/11](auditoria/2026-11-27-auditoria-entrega-1.pdf) ([fonte LaTeX](auditoria/2026-11-27-auditoria-entrega-1.tex)).

## Leia nesta ordem

1. [Auditoria de 27/11](auditoria/2026-11-27-auditoria-entrega-1.pdf): veredito, tabela de requisitos, divergências e o que falta.
2. [Índice das demandas](demandas/README.md): enunciado, as 11 imagens da rubrica e o guia do Overleaf.
3. [Índice da Entrega 1](entregas/entrega-1/README.md): do ZIP até o PDF enviado.
4. [Base editável](entregas/entrega-1/overleaf/main.tex): é aqui que o texto da entrega vai.
5. [Estado do piloto](../docs/piloto/ESTADO.md) e [variação regional](entregas/piloto/piloto_variacao_regional.md): os dados que sustentam a pergunta.

Para uma imersão mais ampla no projeto, há um prompt pronto em [docs/estudo/PROMPT-imersao-projeto-iv.md](../docs/estudo/PROMPT-imersao-projeto-iv.md). Ele cita o caminho local do Pedro; troque pela sua pasta.

## Decisões pendentes do grupo

- **Composição.** A Ficha tem dois integrantes e o enunciado prevê três. Com dois, a mesma pessoa faria as duas conferências da revisão. Confirmar com o professor.
- **Escopo da pergunta.** Proposta: variação regional do tempo até o primeiro acesso documentado a modelos Claude no Bedrock, com atendimento por país como co-primária. Ainda não ratificada.
- **Declaração de uso de IA.** A cópia local do template veda gerar com IA a pergunta, o texto da revisão e as referências, e a base do Overleaf não tem seção de IA. O template original não pôde ser confirmado: baixar de novo o `template-entrega1.zip` da disciplina.

## Regras que valem para a Entrega 1

- A pergunta, a revisão e as referências precisam ser escritas pelo grupo. A minuta em [material-interno/](entregas/entrega-1/material-interno/) foi gerada com IA e serve só como registro.
- Toda obra citada precisa ter sido lida por alguém do grupo e todo DOI testado. Referência não verificável zera a atividade.
- O link na capa é o de leitura (`overleaf.com/read/...`), testado em janela anônima. Escreva cada `#` do endereço como `\#`.

## Como compilar localmente

```bash
cd trabalho-final/entregas/entrega-1/overleaf && tectonic main.tex
```

Depois de editar `overleaf/`, regenere o ZIP com os três arquivos na raiz:

```bash
cd trabalho-final/entregas/entrega-1/overleaf && zip -X ../PCDIV-Entrega1-Overleaf.zip main.tex referencias.bib puclogo.pdf
```

## O que não está no repositório

- Os HTML e JSON brutos do Wayback em `dados/bruto/` ficam fora do Git (`.gitignore`). Os CSV intermediários e as tabelas estão versionados e bastam para reproduzir as contagens do piloto.
- O original do template baixado pelo Pedro ficou fora do repositório; a cópia comparada está em [template-local/](entregas/entrega-1/template-local/).
