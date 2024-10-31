N, S = map(int, input().split())
menor_saldo = S

for _ in range(N):
    movimentacao = int(input())
    S += movimentacao
    if S < menor_saldo:
        menor_saldo = S

print(menor_saldo)
