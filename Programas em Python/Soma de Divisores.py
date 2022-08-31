"""
Escreva um programa que receba como entrada 5 números e exiba aquele cuja soma dos divisores é a maior.

Ex: A soma dos divisores de 4 é 7 (1 + 2 + 4), enquanto a soma dos divisores de 5 é 6 (1 + 5)

Entrada:
Cinco números inteiros

Saída:
Um número inteiro
"""

#Professor pediu para fazer só com funções de repetições ;-;

count = maDiv = div = maNum = meDiv = 0
for i in range(0, 5):
    n = int(input())
    count += 1
    div = 0
    for c in range(1, n+1):
        if n % c == 0:
            div += c
    if count == 1:
        maDiv = div
        maNum = n
    else:
        if div > maDiv:
            maDiv = div
            maNum = n
        if div < meDiv:
            meDiv = div
print(maNum)