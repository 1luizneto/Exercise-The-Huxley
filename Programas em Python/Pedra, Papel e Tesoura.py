"""
Miguel e Maria Rita são irmãos e sempre brigam para resolver quem tem que fazer o quê no apartamento que dividem. 
Então, eles decidiram usar um jogo chamado Pedra, Papel e Tesoura para tomar decisões.

Nesse jogo, cada um tem que escolher que escolher um dos elementos e, de acordo com as regras abaixo, é definido um vencedor:

- Papel enrola Pedra (Papel ganha)
- Pedra amassa Tesoura (Pedra ganha)
- Tesoura corta Papel (Tesoura ganha)

Se forem colocados dois símbolos iguais, o jogo fica empatado.

Para decidir quem vai lavar a louça durante a semana inteira, eles resolveram fazer um campeonato: em 5 partidas sem empates, 
quem conseguir mais vitórias vence e se livra da obrigação.

Escreva um programa que receba como entrada as escolhas de cada irmão a cada partida, e no final exiba o nome daquele que terá que lavar os pratos sujos.

Entrada:
Vários valores String que poderão estar escritos de qualquer maneira

Observe que serão 5 partidas sem empate. Caso haja empate, a partida deverá ser jogada novamente

Saida:
O nome de um dos irmãos em letras maiúsculas

Perceba que quem ganhar o jogo não lavará pratos
"""

#=============================
#Funções


def jokenpo(a, b): #Função para decidir o ganhador do jokenpo
    a = a.upper()
    b = b.upper()
    if a == 'PEDRA' and b == 'TESOURA' or (a == 'PAPEL' and b == 'PEDRA' ) or (a == 'TESOURA' and b =='PAPEL'): 
        a = 1
        b = 0
        return a,b
    elif b == 'PEDRA' and a == 'TESOURA' or (b == 'PAPEL' and a == 'PEDRA' ) or (b == 'TESOURA' and a =='PAPEL'):
       a = 0
       b = 1
       return a,b
    else:
        a = 0
        b = 0
        return a,b

def maior_menor(a ,b): #Função que calcula quem tem mais vitorias
    if a > b:
        return a
    else:
        return b

#=============================
#Programa Principal

maria = miguel = 0
vezes = 0

while True:
    escolha1 = str(input())
    escolha2 = str(input())
    ma, mi = jokenpo(escolha1, escolha2)
    maria += ma
    miguel += mi
    if miguel == 3 or maria == 3: break
    

if maior_menor(maria,miguel) == miguel: print('MIGUEL')
else: print('MARIA')
    
    