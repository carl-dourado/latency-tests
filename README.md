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

