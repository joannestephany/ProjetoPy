import os
from time import sleep
#                 FUNÇÃO PARA ESCOLHER O CARDAPIO - TAMBÉM PRIMEIRA TELA
def escolhaCardapio():
    #global card
    flag = 1
    while flag != 0:
        os.system('cls')
        print("ESCOLHA SEU CARDÁPIO\n")
        print("> 1 Abrir o cardápio de Sorvete")
        print("> 2 Abrir o cardápio de Açai")
        print("> 0 Cancelar e encerra a aplicação.")
        card = input("Escolha: ")
        if card > '2' or card < '0':
            print('Valor inválido, escolha outra opção.')
            sleep(1)
        elif card == '0':
            print("FIM DO PEDIDO!!!")
            sleep(1)
            flag = 0
        else:
            flag = 0      
    return card


#                   FUNÇAO QUE ESCOLHE O TAMANHO DO SORVETE/ACAI
def tamanhosPreco():
    os.system('cls')
    print('DIGITE O NÚMERO CORRESPONDENTE: ')
    print('1 - Pequeno (1 Sabor) 200ml: R$ 4.00')
    print('2 - Médio (2 Sabores) 400ml: R$ 7.00')
    print('3 - Grande (3 Sabores) 600ml: R$ 10.00')
    print('0 - VOLTAR')
    condicao = 1
    while condicao != 0:
        tam = input('Escolha o tamanho: ')
        if tam > '3' or tam < '0':
            print('Opção inválida.')
        else:
            condicao = 0
    return tam
    
            
def cardapio(tam, pedido):  # Após escolher o sabor o pedido do usuário vai par o "carrinho com o sabor e o preço"
    if pedido == '1':
        sabor = ('Chocolate', 'Baunilha', 'Flocos', 'Morango')
        tipo = 'sabor'
        tipos = 'sabores'
        tipo1 = 'Sorvete'
    else:
        sabor = ('Castanha', 'Amendoim', 'Banana', 'Leite em pó')
        tipo = 'acompanhamento'
        tipos = 'acompanhamentos'
        tipo1 = 'Açai'
    flag = 1
    pedidoCliente = []
    while flag != 0:
        limparTela()
        print(f'Nossos {tipos} são: ')
        for i in range(len(sabor)):
            print(f'{i + 1} - {sabor[i]}')
        
        if tam == '1':
            opcao = input(f'Escolha seu {tipo}: ')
            if opcao < '1' or opcao > '4':
                print('Opção inválida')
            else:
                pedidoCliente.append(sabor[int(opcao) - 1])
                print(pedidoCliente)
                pedidoCliente.append(tipo1)
                pedidoCliente.append('Pequeno')
                pedidoCliente.append(4.0)
                flag = 0
        elif tam == '2':
            i = 0
            while i < 2:
                opcao = input(f'Escolha o {i + 1}º {tipo}: ')
                if opcao < '1' or opcao > '4':
                    print('Opção inválida')
                else:
                    pedidoCliente.append(sabor[int(opcao) - 1])
                    print(pedidoCliente)
                    i += 1
            pedidoCliente.append(tipo1)
            pedidoCliente.append('Médio')
            pedidoCliente.append(7.0)
            flag = 0
        else:
            i = 0
            while i < 3:
                opcao = input(f'Escolha o {i + 1}º {tipo}: ')
                if opcao < '1' or opcao > '4':
                    print('Opção inválida')
                else:
                    pedidoCliente.append(sabor[int(opcao) - 1])
                    print(pedidoCliente)
                    i += 1
            pedidoCliente.append(tipo1)
            pedidoCliente.append('Grande')
            pedidoCliente.append(10.0) 
            flag = 0
        sleep(1)        
    return pedidoCliente
   

def cobrar(pTotal):
    limparTela()
    #print('=' * 50)
    print('Pagamento')
    print('O total a ser pago é R$ {:.2f}.'.format(pTotal))
    flag = 1
    while flag != 0:
        valorPago = float(input('Insira o valor em dinheiro: '))
        if valorPago == pTotal:
            print('Compra paga.')
            flag = 0
        elif valorPago != pTotal:
            if valorPago > pTotal:
                limparTela()
                troco = valorPago-pTotal
                print('Compra paga, devolvendo troco.')
                print('Troco: R$ {:.2f}'.format(troco))
                input('Pressione qualquer tecla para confirmar.')
                flag = 0
            else:
                print('Você digitou um valor menor que o valor da compra que é R${}.'.format(pTotal))
                print('Por favor, tente novamente.')

def nota(lista, pTotal):
    limparTela()
    #print('O preço a ser pago é R$ {:.2f}.'.format(pTotal))
    y = 1
    while y != 0:
        cpfnota = input('Deseja CPF na nota? (s/n): ').upper()
        cpf = ''
        if cpfnota == 'S':
            flag = False
            while flag != True:
                cpf = input(f'Digite o cpf: ')
                flag = validarCPF(cpf)
            limparTela()
            print ('=' * 25)
            print(f'Cliente: {nomeCliente}')
            print(f'CPF: {cpf}')
            print('Seu pedido:')
            for i in lista:
                print(f'{i[-3]} {i[-2]}: R$ {i[-1]:.2f}')
            print(f'Total: {pTotal:.2f}')
            print('=' * 25)
            print('Obrigado por visitar a Sorveteria PY! :)')
            y = 0
        elif cpfnota == 'N':
            limparTela()
            print ('=' * 25)
            print(f'Cliente: {nomeCliente}')
            print('Seu pedido:')
            for i in lista:
                print(f'{i[-3]} {i[-2]}: R$ {i[-1]:.2f}')
            print(f'Total: {pTotal:.2f}')
            print('=' * 25)
            print('Obrigado por visitar a Sorveteria PY! :)')
            y = 0
        else:
            print('Opcao inválida')


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


def somarItens(lista):
    somaItens = 0
    for i in lista:
        somaItens += i[-1]
    return somaItens


def limparTela():
    os.system('cls')


def mostrarCarrinho(lista):
    print('Seu carrinho:')
    cont = 0
    for pedido in lista:
        cont += 1
        print('=' * 25)
        if pedido[-3].upper() == 'SORVETE':
            tipo = 'Sabor(es)'
            tipo1 = 'Sorvete'
        else:
            tipo = 'Acompanhamento(s)'
            tipo1 = 'Açai'
        listaSabores = pedido[:] #Clone da lista pedido para lista Sabores
        print(f'Pedido {cont}')
        print(f'{tipo1} {pedido[-2]}: R$ {pedido[-1]:.2f}')
        del listaSabores[-3:] #Apagando os 3 ultimos itens da lista Sabores (Tipo, Tamanho, Preço)
        print(f'{tipo}: ')
        for item in listaSabores:
            print(item, end=' ')
        print()
        print('=' * 25)


def removerItem(lista):
    limparTela()
    mostrarCarrinho(lista)
    flag = 1
    while flag != 0:
        print()
        item = input('Digite o número do pedido que deseja remover (0 - Cancelar): ')
        if item > str(len(lista)) or item < '0':
            print('Item não faz parte da lista.')
        elif item == '0':
            flag = 0
        else:
            lista.pop(int(item) - 1)
            flag = 0
    return lista[:]


def menufinalizarOperacao(lista):
    limparTela()
    mostrarCarrinho(lista)
    print('\n1 - Adicionar novo pedido ao carrinho.')
    print('2 - Remover um pedido do carrinho.')
    print('3 - Finalizar a operação')
    resp = input('Digite a opção: ')
    return resp


# FUNÇÃO PRINCIPAL
limparTela()
print('BEM VINDO À SORVETERIA PY \n')
global nomeCliente
nomeCliente = input('Digite seu nome para começarmos: ')
flag = 1
carrinho = [] 
precoTotal = 0
#PRIMEIRO MENU
while flag != 0:
    pedido = escolhaCardapio()
    #SEGUNDO MENU OPCAO 1 - SORVETE
    if pedido == '1': # Sorvete 
        tamanho = tamanhosPreco()
        if tamanho == '0':
            pass
        #TERCEIRO MENU - ESCOLHER SABOR
        else: 
            carrinho.append(cardapio(tamanho, pedido))
            precoTotal = somarItens(carrinho)
            print()
            print(f'Subtotal: R$ {precoTotal:.2f}')
            laco = 1
            while laco != 0:
                resp = menufinalizarOperacao(carrinho)
                if resp > '3' or resp < '1':
                    print('Opção inválida')
                elif  resp == '1':
                    laco = 0
                    pass
                elif resp == '2':
                    carrinho = removerItem(carrinho)
                else:
                    cobrar(precoTotal)
                    nota(carrinho, precoTotal)
                    print('Pedido Finalizado.')
                    laco = 0
                    flag = 0
            sleep(1)
    #SEGUNDO MENU OPCAO 2 - AÇAI
    elif pedido == '2': # Açai
        tamanho = tamanhosPreco()
        if tamanho == '0':
            pass
        #TERCEIRO MENU - ESCOLHER SABOR
        else:
            carrinho.append(cardapio(tamanho, pedido))
            precoTotal = somarItens(carrinho)
            print()
            print(f'Subtotal: R$ {precoTotal:.2f}')
            laco = 1
            while laco != 0:
                resp = menufinalizarOperacao(carrinho)
                if resp > '3' or resp < '1':
                    print('Opção inválida')
                elif  resp == '1':
                    laco = 0
                    pass
                elif resp == '2':
                    carrinho = removerItem(carrinho)
                else:
                    cobrar(precoTotal)
                    nota(carrinho, precoTotal)
                    print('Pedido Finalizado.')
                    laco = 0
                    flag = 0
            sleep(1)
    else:
        flag = 0

