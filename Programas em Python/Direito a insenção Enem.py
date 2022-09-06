def semTaxa(se=0, enc=0, encN=0, tes=0, renda=0):
    sel = ['CLD','CVC','CSC','NCC']
    tesL = ['PUB','PCB','PSB','PPS','PPB','NFE']
    if se.upper() in sel:
        if se.upper() == 'NCC':
            return f'Infelizmente voce nao tem direito a isencao'
        if se.upper() == 'CVC':
            if tes.upper() in tesL:
                if tes.upper() == 'PUB' or tes.upper() == 'PCB':
                    return f'Voce terah direito a isencao'
            else:
                return f'Informacao sobre ensino medio invalida'
        if se.upper() in 'CLD':
            if renda < 1431:
                return f'Voce terah direito a isencao'
    else: 
        return f'Informacao sobre ensino medio invalida'
    if enc == 's':
        if tes.upper() in tesL:
            if tes.upper() == 'PUB' or tes.upper() == 'PCB' :
                if encN >= 400:
                    return f'Voce terah direito a isencao'
                else:
                    if renda < 1431:
                        return f'Voce terah direito a isencao'
                    return f'Infelizmente voce nao tem direito a isencao'
            else:
                return f'Infelizmente voce nao tem direito a isencao'
        else:
            return f'Informacao sobre ensino medio invalida'
     

sitEm = str(input())
enceja = str(input())
encejaN = int(input())
tipoEs = str(input())
rendaP = float(input())
resultado = semTaxa(sitEm, enceja, encejaN, tipoEs, rendaP)

print(resultado)