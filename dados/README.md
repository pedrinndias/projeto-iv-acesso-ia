# Dados

## Regra principal

`bruto/` é imutável. Arquivos entram aqui exatamente como vieram da fonte e não são
editados. Correção e limpeza acontecem em `src/tratamento/`, com saída em `intermediario/`.

## Proveniência

Todo arquivo em `bruto/` deve ter, no nome ou em um `.meta.json` ao lado:

- a URL de origem
- a data e hora da coleta
- o script que o gerou

## Fontes previstas

| Arquivo | Fonte | Script |
|---|---|---|
| `aws_servicos_regiao_AAAA-MM-DD.json` | Índice público de serviços por região da AWS | `src/coleta/servicos_por_regiao_aws.py` |
| `cobertura_wayback_AAAA-MM-DD.csv` | API CDX do Internet Archive | `src/coleta/cobertura_wayback.py` |

## Aviso

Arquivos JSON e HTML em `bruto/` estão no `.gitignore` por causa do tamanho. Quem precisar
reproduzir a base roda os scripts de coleta. O que é versionado é o **código que gera o dado**,
não o dado em si.
