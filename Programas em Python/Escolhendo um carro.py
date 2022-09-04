espacoInterno = str(input()).upper()
portaMalas = str(input()).upper()
valorCarro = float(input())
motor = float(input())
cambio = str(input()).upper()
cont = 0
contOb = 0

if espacoInterno == 'A':
    contOb += 1
if portaMalas == 'G':
    contOb += 1
if valorCarro < 100000:
    cont += 1
if motor >= 1.5:
    cont += 1
if cambio == 'A':
    cont += 1


if cont == 3 and contOb == 2:
    print('Pode comprar!')
elif cont == 2 and contOb == 2:
    print('Boa compra.')
elif cont == 1 and contOb == 2:
    print('Pode ser uma op��o.')
else:
    print('N�o compre!')