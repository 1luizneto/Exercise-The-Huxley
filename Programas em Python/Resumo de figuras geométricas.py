"""
Escreva um programa que recebe informações de várias figuras geométricas  e, em seguida, 
imprime um resumo das características (área e comprimento) dessas figuras. 
O programa pode receber até 3 tipos de figuras: quadrado, retângulo e círculo, identificados pela primeira letra da figura. 
Caso as dimensões da figura forem negativas, o resultado do cálculo das características será -1. 
O programa encerrará quando o usuário digitar sair no tipo da figura.

Use funções para modularizar seu programa. Faça uma função para cada cálculo de característica de uma figura. 
Faça também uma função para imprimir o resumo final.

Obs.: Use pi = 3.14 e o resultado com 2 casas decimais de aproximação.

Entrada:
Várias informações de figuras geométricas em sequência:

Tipo da figura: (q)uadrado, (r)etângulo, (c)írculo
Em seguida
Se a figura for um quadrado, receba o lado do quadrado
Se a figura for um retângulo, receba a medida da base e da altura
Se a figura for um círculo, receba o valor do raio

Saída:
Seu programa deve imprimir no final as seguintes informações:

Os valores das maiores figuras de cada tipo
O número total de figuras
O percentual de figuras que são círculos
"""

#=============================
#Funções

def quadrado(l):    #Função para calcular o quadrado
    l = int(l)
    if l == -1:    
        area = -1
        return area
    area = l * l
    return area


def retangulo(b, a):    #Função para calcular o quadrado
    b = int(b)
    a = int(a)
    if b == -1 or a == -1:
        area = -1
        return area
    area = b * a
    return area


def circulo(r):     #Função para calcular o quadrado
    r = int(r)
    if r == -1:
        area = -1
        return area
    area = 3.14 * (r**2)
    return area

#=============================
#Programa Principal

rt = []
qua = []
cir = []

while True: #Loop que recebe os valores calculados
    escolha = str(input()).upper()
    if escolha == 'SAIR': break
    if escolha == 'R':
        base = int(input())
        altura = int(input())
        rt.append(float(retangulo(base, altura)))
    if escolha == 'Q':
        lado = int(input())
        qua.append(float(quadrado(lado)))
    if escolha == 'C':
        raio = int(input())
        cir.append(float(circulo(raio)))

quantidade = len(cir)+len(rt)+len(qua)
percentual = (len(cir)/quantidade)*100

print(f'Maior circulo: {max(cir):.2f}')
print(f'Maior retangulo: {max(rt):.2f}')
print(f'Maior quadrado: {max(qua):.2f}')
print(f'Quantidade de figuras {quantidade}')
print(f'Percentual de circulos: {percentual:.2f}')