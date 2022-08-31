"""
Uma agência de turismo resolveu fazer um cadastro das hospedagens mais populares da Paraíba, 
e para isso pediu que seus clientes fizessem uma classificação de qualidade, indicando quantas estrelas (de 1 a 5) cada hotel merecia.

Escreva um programa que receba como entrada o tipo (hotel ou pousada), 
a quantidade de estrelas e a cidade de 10 estabelecimentos e exiba quantos hotéis em João Pessoa são 5 estrelas, 
qual a média de estrelas dos estabelecimentos de Campina Grande, e quantas pousadas existem em Rio Tinto.

Entrada:
Um String, um inteiro e outro String para cada estabelecimento

Dica: os usuários podem usar minúsculas e/ou maiúsculas nos Strings

Saída:
Três valores inteiros
"""

#Professor pediu para fazer só com funções de repetições ;-;

H5s = MCh = PRt = count = 0
for i in range(0, 10):
    hotel = str(input()).upper()
    estrelas = int(input())
    cidade = str(input()).upper()
    if hotel in 'HOTEL' and estrelas == 5 and cidade in 'JOAO PESSOA':
        H5s += 1
    if cidade in 'CAMPINA GRANDE':
        MCh += estrelas
        count += 1
    if hotel in 'POUSADA' and cidade in 'RIO TINTO':
        PRt +=1
print(H5s)
if count == 0:
    print(MCh)
else:
    print(f'{MCh / count:.0f}')
print(PRt)        