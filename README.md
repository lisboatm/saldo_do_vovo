# Vovô João e Sua Banca de Jornais

## Descrição

Vovô João tem uma banca de jornais e realiza diariamente depósitos e retiradas em sua conta bancária. O saldo pode ficar negativo em alguns dias, e a tarefa é calcular o menor saldo que a conta alcança durante um determinado período.

## Objetivo

Escrever um programa que receba as movimentações diárias da conta do Vovô João e determine o menor saldo durante o período especificado.

## Entrada

A entrada consiste em:
1. A primeira linha contém dois números inteiros:
   - `N`: o número de dias do período de interesse (1 ≤ N ≤ 30).
   - `S`: o saldo da conta no início do período (−10³ ≤ S ≤ 10³).

2. As próximas `N` linhas contêm um número inteiro cada, que representa a movimentação do dia:
   - Um valor positivo representa um depósito.
   - Um valor negativo representa uma retirada.
   - Cada movimentação pode variar de (−10³ ≤ movimentação ≤ 10³).

## Saída

O programa deve imprimir uma única linha com um número inteiro, que representa o menor saldo da conta durante o período dado.

## Exemplo de Entrada e Saída

### Exemplo 1

#### Entrada:
```
3 1000
100
-800
50
```

#### Saída:
```
300
```

### Exemplo 2

#### Entrada:
```
6 -200
-100
1000
-2000
100
-50
2000
-1300
```

#### Saída:
```
-1300
```

## Implementação

Um exemplo de implementação em Python pode ser:

```python
N, S = map(int, input().split())
menor_saldo = S

for _ in range(N):
    movimentacao = int(input())
    S += movimentacao
    if S < menor_saldo:
        menor_saldo = S

print(menor_saldo)
```

## Notas

- O programa deve calcular o saldo diário com base nas movimentações fornecidas.
- A saída deve ser o menor saldo encontrado durante o período analisado.
