"""
Nos estudos sobre as Leis da Termodinâmica, considerando conservação de energia e funcionamento de máquinas térmicas, 
aprende-se sobre o calor de fontes quentes e frias e as trocas entre elas.

Para automatizar os cálculos relacionados às fontes quentes e frias, 
vamos criar um programa que determine o calor recebido por uma fonte quente e perdido por uma fonte fria de motores a diesel.

Sabe-se da Termodinâmica que:

O rendimento (R) do motor a diesel é a razão do trabalho (t) executado em cada ciclo pela quantidade total de energia fornecida pela fonte quente (Q1):
R = t ÷ Q1
O calor fornecido pela fonte quente (Q1) é igual à soma do trabalho (t) realizado pela máquina com o calor perdido para a fonte fria (Q2):
Q1 = t + Q2
Serão informados o rendimento de um motor e o trabalho realizado a cada ciclo do referido motor. 
Seu programa deve funcionar para várias entradas e parar quando o valor do rendimento lido for maior ou igual a 100% 
(já que nenhuma máquina térmica tem 100% de eficiência).



Obs_1.: Forneça as respostas em calorias. Sabendo que: 1 cal = 4 J.

Obs_2.: Crie pelo menos duas funções (pode ter mais), uma para calcular a energia fornecida pela fonte quente, 
e a outra para calcular o calor perdido para a fonte fria.

Entrada:
O percentual de rendimento (R) do motor;
O trabalho realizado em cada ciclo, em Joule (J).

Saída:
O calor recebido da fonte quente e perdido para a fonte fria, em calorias, e com duas casas decimais.
"""

#=============================
#Funções

def fonte_quente(R ,J):
    Q1 = J / (R/100)
    return f'{Q1/4:.2f}'

def fonte_fria(R, J):
    Q1 = J / (R/100)
    Q2 = Q1 - J
    return f'{Q2/4:.2f}'

#=============================
#Programa Principal

while True:
    r = float(input())
    if r >= 100: break
    else:
        j = int(input())
        print(f'Q1 = {fonte_quente(r,j)} cal')
        print(f'Q2 = {fonte_fria(r,j)} cal')




