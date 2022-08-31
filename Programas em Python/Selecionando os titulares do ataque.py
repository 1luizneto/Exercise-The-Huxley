"""
Faça uma função que escolhe o ataque titular da seleção brasileira baseado nas características de cada jogador. 
Cada característica será usada para compor um índice técnico que será usado para definir os titulares.

Seu programa deve receber:

O nome do jogador
Seu desempenho no treino (bom, mediano, ruim)
Quantos gols ele fez no último jogo
Qual o seu nível de cansaço (muito cansado, pouco cansado, descansado)
Seu nível de entrosamento com os companheiros (alto, médio ou baixo)
No final, o programa deve imprimir os índices técnicos dos três jogadores que devem ser os titulares do ataque do Brasil.

O índice técnico deve ser calculado da seguinte forma:

Um jogador não pode ter 2 características no nível mínimo seu índice será zero. Caso contrário, o índice será calculado da seguinte forma:

índice = desempenho_no_treino*2 + numero_de_gols*3.5 + cansaço*1.5 + entrosamento*2

O programa pára quando receber 5 jogadores.

"""

#=============================
#Funções

def calcDesempenho(d, g, nc, e):
    return d*2 + g*3.5 + nc*1.5 + e*2  #Função para calcular o desempenho dos jogadores

def titulares(a):
    a.sort()
    maiores = a[-3:]
    q = sorted(maiores, reverse=True) #Função que mostra os três jogadores com melhor desempenho
    for c in range(0, len(q)):
        print(f'{q[c]}')

#=============================
#Programa Principal

lista = []

for c in range(0, 5):
    nome = str(input())
    desem = int(input())
    gols = int(input())
    can = int(input())
    entro = int(input())

    lista.append(calcDesempenho(desem, gols, can, entro))

titulares(lista)