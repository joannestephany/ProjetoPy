import os
#                 FUNÇÃO PARA ESCOLHER O CARDAPIO - TAMBÉM PRIMEIRA TELA
def escolhaCardapio():
    #global card
    card = 1
    while card != 0:
        os.system('cls')
        print("ESCOLHA SEU CARDÁPIO\n")
        print(" > Digite 1 para abrir o caradápio de Sorvete")
        print(" > Digite 2 para abrir o cardápio de Açai")
        print(" > Digite 0 Finalizar pedido.")

        card = int(input(" Escolha: "))
        if card == 1:
            return card
        elif card == 2:
            return card
        elif card == 0:
            print("FIM DO PEDIDO!!!")  # tem que chamar a função aqui que calcula tudo
            return card
        else:
            print('Valor inválido, escolha outra opção.')


#                   FUNÇAO QUE ESCOLHE O TAMANHO DO SORVETE/ACAI (CHAMA FUNCAO MENU SORVETE/ACAI)
def tamanhosPreco():
    os.system('cls')
    print('DIGITE O NÚMERO CORRESPONDENTE: ')
    print('1 - PEQUENO 200ml: 4,00 R$ ')
    print('2 - MEDIO 400ml: 7,00 R$')
    print('3 - GRANDE 600ml: 10,00 R$')
    print('0 - VOLTAR')
    condicao = 1
    preco = 0.0
    while condicao != 0:
        tam = int(input('Escolha o tamanho: '))
        if tam == 1:
            preco = 4
            return preco
        elif tam == 2:
            preco = 7
            return preco
        elif tam == 3:
            preco = 10
            return preco
        elif tam == 0:
            return 0
        else:
            print('Opção inválida.')



def cardSorvete(tam):  # Após escolher o sabor o pedido do usuário vai par o "carrinho com o sabor e o preço"
    sabor = ('Chocolate', 'Baunilha', 'Flocos', 'Morango')
    print("Nossos sabores são: ")
    for i in range(len(sabor)):
        print(f'{i + 1} - {sabor[i]}')
    seusSabores = []
    while len(seusSabores) < tam:
        print("Escolha seu {}º sabor.".format(len(seusSabores) + 1))
        nomeDoSabor = input()
        seusSabores.append(nomeDoSabor)
    print("Seus sabores foram: {}".format(seusSabores))


def cardAcai(tam):  # Após escolher o sabor o pedido do usuário vai par o "carrinho com o sabor e o preço"
    complementos = list()
    complementos.append('Castanha')
    complementos.append('Amendoim')
    complementos.append('Banana')
    complementos.append('Achocolatado')
    print("Nossos complementos são: {}".format(complementos))
    seusComplementos = []
    print("Você tem direito a {} complemento(s)".format(tam))
    while len(seusComplementos) < tam:

        print("Escolha seu {}º complemento.".format(len(seusComplementos) + 1))
        nomeDoComp = input()
        seusComplementos.append(nomeDoComp)
    print("Seus complementos foram: {}".format(seusComplementos))


def fimPedido():  # nessa função quando for encerrar vai fazer o calculo dos itens pedidos
    print("fim")  # só para ter alguma coisa


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




'''
PARAMOS NESSA FUNÇAO
'''
print('BEM VINDO À SORVEETERIA PY \n')
nomeCliente=input("Digite seu nome para começarmos: ")
pedido = 1
while pedido != 0:
    pedido = escolhaCardapio()
    if pedido == 1: # Sorvete 
        preco = tamanhosPreco()
        cardSorvete(preco)
    elif pedido == 2: # Açai
        preco = tamanhosPreco()
        cardAcai(preco)
    elif pedido == 0:
        #Chamar função nota
        None
    else:
        None
print(nomeCliente)
'''
print(preco) vai mostrar o valor que a pessoa ter que pagar
print(seusComplementos) vai mostrar os complementos  escolhidos
print(seusSabores) vai mostrar os sabores escolihods
!!!falta colocar condição caso a pessoa digite um sabor que não tenha (usando string).requisito
!!!falta repetir o programa caso a pessoa queira pedir outro produto e acumular na variavel preco
!!!falta usar valores boleanos(true/false).requisito
!!!condicao aninhada/encadeada.requisito
'''
# card = escolhaCardapio()

