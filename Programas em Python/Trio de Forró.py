"""
Um trio de forró de Campina Grande vai começar a organizar a agenda de shows para o mês de junho que se aproxima, o mês do São João.


     Algumas condições são necessárias para que o trio aceite um contrato para tocar em uma festa. 
     Eles partem de um valor base para contratação de R$ 1.000,00, e o restante do valor vai ser acrescido dependendo de outros fatores que são:

Se a distância entre as cidades for de até 50 Km, acrescentar R$ 5,00 a cada quilômetro;
Se a distância entre as cidades for de 51 Km até 100 Km, acrescentar R$ 6,50 a cada quilômetro;
Se a distância entre as cidades for de mais de 100 Km, acrescentar R$ 10,00 a cada quilômetro;
Se a distância entre as cidades for maior que 500 Km, o trio rejeita o contrato;
     Outro ponto que o trio faz questão que seja cumprido é que eles façam, no máximo, 6 shows a cada 10 dias. Lembre-se, o mês de junho tem 30 dias.
     Sabendo que você é um excelente programador, o trio pediu sua ajuda para organizar a agenda de shows, para que eles tenham uma ideia de quanto em dinheiro será arrecadado no mês, obedecendo às restrições citadas.
     Faça um programa que receba várias entradas com intenções de contratação, e informe:
Qual será a quantia arrecadada pelo trio ao final do mês de junho;
Em quantas festas eles irão tocar;
Quantas intenções de contratação foram recusadas, por questões de distância e por datas;
E, caso haja contratação(ões), você também deve informar quantos shows serão realizados em cada período de 10 dias do mês de junho.

Entrada:
Você deve ler, repetidamente, a informação da distância para a cidade que deseja contratar o trio (será um número inteiro).
 Quando a entrada lida for um valor menor que 0 (zero), o programa deve parar e exibir os resultados. Distância igual a zero indica show em Campina Grande.

     E um inteiro informando em qual período do mês será a festa contratada, da seguinte forma:

1 se a festa for de 01/06 a 10/06;
2 se a festa for de 11/06 a 20/06;
3 se a festa for de 21/06 a 30/06.

Saída:
O valor que será arrecadado com todos os shows do mês de junho, com duas casas decimais;
Quantidade de shows que serão realizados;
Quantidade de shows recusados por data;
Quantidade de shows recusados por distância;
Quantos shows serão realizados a cada 10 dias;
    Veja mensagens utilizadas na saída na tabela com exemplos de Entrada / Saída, abaixo.
"""

#Professor pediu para fazer só com funções de repetições ;-;

valorTotal = countSh = rejeitadoDi =  rejeitadoDa = sD1 = sD2 = sD3 = valorShow = sD1t = sD2t = sD3t = 0
passa = passaSd1 = passaSd2 = passaSd3 = 0
contratacao = 1000
while True:
    distancia = int(input())
    if distancia < 0:
        print(f'Arrecadado: R$ {valorTotal:.2f}')
        print(f'Quantidade de Shows: {countSh}')
        print(f'Shows Recusados por Data: {rejeitadoDa}')
        print(f'Shows Recusados por Distancia: {rejeitadoDi}')
        if sD1 > 0 or sD2 > 0 or sD3 > 0:
            print(f'Shows de 01 a 10/06: {sD1} festa(s)\nShows de 11 a 20/06: {sD2} festa(s)\nShows de 21 a 30/06: {sD3} festa(s)')
        break
    if distancia >= 500:
        rejeitadoDi += 1
    else:
        diaShow = int(input())
        if diaShow == 1:
            sD1t += 1
        if diaShow == 2:
            sD2t += 1
        if diaShow == 3:
            sD3t += 1
        if diaShow == 1 and sD1 < 6:
            sD1 += 1
            if distancia == 0:
                valorTotal += contratacao
                countSh += 1
                passa = 1
            if 1 < distancia <= 50:
                valorTotal += contratacao
                countSh += 1
                passa = 1
                for i in range(0, distancia):
                    valorTotal += 5
            elif 51 <= distancia <= 100:
                valorTotal += contratacao
                countSh += 1
                passa = 1
                for i in range(0, distancia):
                    valorTotal += 6.50
            elif 100 < distancia < 500:
                valorTotal += contratacao
                countSh += 1
                passa = 1
                for i in range(0, distancia):
                    valorTotal += 10
        elif diaShow == 2 and sD2 < 6:
            sD2 += 1
            if distancia == 0:
                valorTotal += contratacao
                countSh += 1
                passa = 1
            if 1 < distancia <= 50:
                valorTotal += contratacao
                countSh += 1
                passa = 1
                for i in range(0, distancia):
                    valorTotal += 5
            elif 51 <= distancia <= 100:
                valorTotal += contratacao
                countSh += 1
                passa = 1
                for i in range(0, distancia):
                    valorTotal += 6.50
            elif 100 < distancia < 500:
                valorTotal += contratacao
                countSh += 1
                passa = 1
                for i in range(0, distancia):
                    valorTotal += 10
        elif diaShow == 3 and sD3 < 6:
            sD3 += 1
            if distancia == 0:
                valorTotal += contratacao
                countSh += 1
                passa = 1
            if 1 < distancia <= 50:
                valorTotal += contratacao
                countSh += 1
                passa = 1
                for i in range(0, distancia):
                    valorTotal += 5
            elif 51 <= distancia <= 100:
                valorTotal += contratacao
                countSh += 1
                passa = 1
                for i in range(0, distancia):
                    valorTotal += 6.50
            elif 100 < distancia < 500:
                valorTotal += contratacao
                countSh += 1
                passa = 1
                for i in range(0, distancia):
                    valorTotal += 10
        else:
            if diaShow > 3:
                rejeitadoDa += 1
            rejeitadoDa = (sD1t - sD1) + (sD2t - sD2) + (sD3t - sD3)




