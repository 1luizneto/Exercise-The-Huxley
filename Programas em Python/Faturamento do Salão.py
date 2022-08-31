"""
No salão de Ambrósio atende-se tanto homens quanto mulheres.

No caso dos homens, eles podem cortar o cabelo ou simplesmente fazer a barba. Mas nunca ambos. O corte de cabelo custa R$ 25,00 e a barba custa R$ 15,00.

Já as mulheres podem cortar o cabelo ao custo de R$ 40,00,  fazer o penteado ao custo de R$ 50,00 ou se maquiar pagando R$ 70,00.

No fim do dia, Ambrósio quer saber qual foi o serviço mais executado pelos homens. 
Além disso, ele quer saber também qual foi o faturamento total daquele dia.

Entrada:
A entrada consiste de várias sequências de 2 linhas. 
A primeira linha contém uma string com o sexo (M ou F escritos em maiúsculo ou minúsculo).
A segunda linha contém descrição do serviço desejado por cada cliente. Os serviços podem ser: "corte", "barba" , "maquiagem" ou "penteado". 
Os serviços também podem com caracteres maiúsculo ou minúsculos.

A entrada será encerrada quando for informado um sexo diferente de M e F.

Saida:
Uma string (em maiúsculo) com o nome do serviço mais usado pelos homens (CORTE ou BARBA). Em caso de empate, deverá ser exibida a mensagem AMBOS.

No caso onde não existam clientes homens, será considerado um empate.

Um valor real com duas casas decimais para o faturamento do salão.
"""

#Professor pediu para fazer só com funções de repetições ;-;

totalValor = countB = countC = 0

while True:
    sexo = str(input()).upper()
    if sexo not in 'MF':
        if countB > countC:
            print('BARBA')
        elif countB < countC:
            print('CORTE')
        elif countB == countC:
            print('AMBOS')
        print(f'{totalValor:.2f}')
        break
    servico = str(input()).upper()
    if sexo == 'M':
        if servico in 'BARBA':
            totalValor += 15
            countB += 1
        elif servico in 'CORTE':
            totalValor += 25
            countC += 1
    if sexo == 'F':
        if servico in 'CORTE':
            totalValor += 40
        elif servico in 'PENTEADO':
            totalValor += 50
        elif servico in 'MAQUIAGEM':
            totalValor += 70
