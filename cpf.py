def validarCPF(cpf):
    if cpf.count(cpf[1]) == 11:
        print('CPF inválido, confira os dados.')
    elif len(cpf) != 11:
        print('CPF inválido, confira os dados.')  
    else:    
        soma1 = 0
        cont = 10
        for i in range(2, 11):
            soma1 += (int(cpf[i - 2]) * cont)
            cont -= 1

        resto = (soma1 * 10) % 11
        if resto != 10 and resto != int(cpf[-2]):
            print('CPF inválido, confira os dados.')
        else:
            soma2 = 0
            cont = 11
            for x in range(2, 12):
                soma2 += (int(cpf[x - 2]) * cont)
                cont -= 1

            resto = (soma2 * 10) % 11
            if resto != int(cpf[-1]):
                print('CPF inválido, confira os dados.')
            else:
                print('CPF Válido!')
                return True


def menuCPF():
    flag = False
    while flag != True:
        opt = input(f'Digite o cpf ou Apenas 0 para cancelar: ')
        if int(opt) != 0:
            flag = validarCPF(opt)
        else:
            print('Operação cancelada.')
            flag = True


menuCPF()
