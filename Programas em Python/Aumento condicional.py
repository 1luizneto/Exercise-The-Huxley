def reajuste(salario):
    if salario <= 280:
            return f'{salario:.2f}\n20\n{salario*0.2:.2f}\n{(salario*0.2)+salario:.2f}'
    elif salario > 280 and salario < 700:
        return f'{salario:.2f}\n15\n{salario*0.15:.2f}\n{(salario*0.15)+salario:.2f}'
    elif salario > 700 and salario < 1500:
        return f'{salario:.2f}\n10\n{salario*0.1:.2f}\n{(salario*0.1)+salario:.2f}'
    else:
        return f'{salario:.2f}\n5\n{salario*0.05:.2f}\n{(salario*0.05)+salario:.2f}'
    

#prog

salario = float(input())
valor = (reajuste(salario))
print(valor)