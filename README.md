# latency-tests

Teste simples para juntar alguns numeros de latencia.

Eu uso isso para parar de ficar no "acho que esta lento". O script roda ping algumas vezes, calcula media, p95 e uma ideia simples de jitter.

## uso

```bash
python latency_tests.py
```

Mudando alvo e rodadas:

```bash
python latency_tests.py --target 1.1.1.1 --rounds 10
```

Salvando CSV:

```bash
python latency_tests.py --csv latencia.csv
```

## notas

- feito para Linux
- usa `ping`
- os numeros sao pequenos, so para comparar depois

## limites

- o p95 e calculado de forma simples, suficiente para poucas amostras
- nao separa perda de pacote por motivo
- nao tem modo daemon nem historico automatico
- depende do formato da saida do `ping`

## coisas para melhorar depois

- validar melhor `--rounds`, `--interval` e `--timeout`
- adicionar testes para `summarize` e `percentile`
- salvar tambem um resumo em CSV
- comparar dois alvos na mesma execucao

## anotacoes de aprendizado

A ideia foi transformar algumas rodadas de `ping` em numeros mais faceis de comparar. O script ainda e simples, mas ja ajuda a treinar parsing, estatistica basica e escrita de CSV.
