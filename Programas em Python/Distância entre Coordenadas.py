"""
A distância entre os pontos A e B é a medida do segmento que tem os dois pontos como extremidade. 
Por se tratar de dois pontos quaisquer, representaremos as coordenadas desses pontos de maneira genérica.
Dessa forma para calcular a distância entre dois pontos faz-se necessário utilizar a seguinte fórmula (distância euclidiana):



Escreva um programa que leia um conjunto de N pares de pontos representados por suas coordenadas  X e Y,
 mostrando como resultado a distância euclidiana entre cada um destes pontos.

A distância euclidiana tem que ser calculada por uma função chamada distancia, a qual recebe como parâmetros as coordenadas Xa, Ya, Xb e Yb, 
retornando como resultado a distância entre os pontos A e B

Entrada:
Na primeira linha deve ser lido o valor de N, que representa quantos pares de pontos serão lidos nas linhas seguintes.

As N linhas seguintes terão 4 inteiros separados entre si por um espaço em branco dispostos na mesma linha. 
Os dois primeiros representam na sequência as coordenados x e y do ponto A e os dois últimos as coordenadas x e y do ponto B

Saida:
Para cada par de pontos, deve ser impresso um número real (ponto flutuante) com 2 casas decimais representando a distância euclidiana entre os pontos A e B.
"""
#=============================
#Funções

def coordenadas(xa, ya, xb, yb): #Função para calcular a distancia entre dois pontos
    xa = int(xa)
    xb = int(xb)
    ya = int(ya)
    yb = int(yb)
    d = 0
    d = ((xb-xa)**2)+((yb -ya)**2)
    d = d ** 0.5
    return f'{d:.2f}'


#=============================
#Programa Principal


nl = int(input())
for i in range(0, nl):
    xa , xb, ya, yb = input().split()
    print(coordenadas(xa, xb, ya, yb))