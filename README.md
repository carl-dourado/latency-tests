# latency-tests

Esse repo nasceu como um complemento do `ping-lab`.

No `ping-lab` eu queria testar alguns alvos. Aqui eu queria repetir o teste varias vezes e guardar os numeros para comparar depois, sem ficar no "parece lento".

E um script pequeno, mas ja mostra coisa util: quantas tentativas passaram, media, p95, maximo e uma ideia simples de jitter.

## o que tem aqui

- CLI em Python
- varias rodadas de `ping`
- alvo configuravel
- intervalo entre testes
- timeout configuravel
- resumo no terminal
- exportacao para CSV

## rodando

```bash
python latency_tests.py
```

Mudando alvo e quantidade de rodadas:

```bash
python latency_tests.py --target 1.1.1.1 --rounds 10
```

Sem esperar entre uma rodada e outra:

```bash
python latency_tests.py --target 127.0.0.1 --rounds 5 --interval 0
```

Salvando CSV:

```bash
python latency_tests.py --csv latencia.csv
```

## o que eu treinei

- argumentos no terminal com `argparse`
- execucao de comando do sistema com `subprocess`
- leitura da latencia retornada pelo `ping`
- calculo de media, p95 e jitter
- escrita de CSV para analisar depois

## limites

- o p95 e calculado de forma simples, suficiente para poucas amostras
- nao separa perda de pacote por motivo
- nao tem modo daemon nem historico automatico
- depende do formato da saida do `ping`

## o que falta

- validar melhor `--rounds`, `--interval` e `--timeout`
- adicionar testes para `summarize` e `percentile`
- salvar tambem um resumo em CSV
- comparar dois alvos na mesma execucao
- gerar grafico a partir do CSV
- testar melhor comportamento quando a rede falha muito

## nota

O p95 aqui e mais uma referencia simples. Com poucas rodadas ele nao deve ser tratado como estatistica perfeita. A ideia do repo e estudo e comparacao rapida.
