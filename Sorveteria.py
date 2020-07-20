import os


#                 FUNÇÃO PARA ESCOLHER O CARDAPIO - TAMBÉM PRIMEIRA TELA
def escolhaCardapio():
    global card
    card = 1
    while card != 0:
        print("ESCOLHA SEU CARDÁPIO\n")
        print(" > Digite 1 para abrir o caradápio de Sorvete")
        print(" > Digite 2 para abrir o cardápio de Açai")
        print(" > Digite 0 Finalizar pedido.")

        card = int(input(" Escolha: "))
        if card == 1:
            tamanhosPreco(card)
        elif card == 2:
            tamanhosPreco(card)
        elif card == 0:
            print("FIM DO PEDIDO!!!")  # tem que chamar a função aqui que calcula tudo
            break
        else:
            print('Valor inválido, escolha outra opção.')


#                FUNÇÃO QUE MOSTRA MENU SORVETE - INCOMPLETA
def cardSorvete(preco):  # Após escolher o sabor o pedido do usuário vai par o "carrinho com o sabor e o preço"
    sabores = list()
    sabores.append('1 - Chocolate')
    sabores.append('2 - Baunilha')
    sabores.append('3 - Flocos')
    sabores.append('4 - Morango')
    print(sabores)
    return sabores


#               FUNÇÃO QUE MOSTRA MENU ACAI - INCOMPLETA
def cardAcai(tam):  # Após escolher o sabor o pedido do usuário vai par o "carrinho com o sabor e o preço"
    complementos = list()
    complementos.append('Castanha')
    complementos.append('Amendoim')
    complementos.append('Banana')
    complementos.append('Achocolatado')
    print("Nossos complementos são: {}".format(complementos))
    seusComplementos = []
    print(tam)
    while len(seusComplementos) < tam+2:
        print("Escolha seu {}º complemento.".format(len(seusComplementos) + 1))
        nomeDoComp = input()
        seusComplementos.append(nomeDoComp)
    print("Seus complementos foram: {}".format(seusComplementos))


def fimPedido():  # nessa função quando for encerrar vai fazer o calculo dos itens pedidos
    print("fim")  # só para ter alguma coisa


#                   FUNÇAO QUE ESCOLHE O TAMANHO DO SORVETE/ACAI (CHAMA FUNCAO MENU SORVETE/ACAI)
def tamanhosPreco(opt):
    print('DIGITE O NÚMERO CORRESPONDENTE: ')
    print('1 - PEQUENO = 200ml = 4,00 R$ ')
    print('2 - MEDIO = 400ml = 7,00 R$')
    print('3 - GRANDE = 600ml = 10,00 R$')
    print('0 - VOLTAR')
    condicao = 1
    preco = 0
    while condicao != -1:
        tam = int(input('Escolha o tamanho: '))
        if tam == 1 or tam == 2 or tam == 3 or tam == 0:
            if tam == 1:
                preco = 4
                condicao = -1
            elif tam == 2:
                preco = 7
                condicao = -1
            elif tam == 3:
                preco = 10
                condicao = -1
            elif tam == 0:
                return
            else:
                print('Opção inválida.')
    if opt == 1:
        cardSorvete(tam)
    else:
        cardAcai(tam)


'''
PARAMOS NESSA FUNÇAO
'''
print('BEM VINDO À SORVEETERIA PY \n')
escolhaCardapio()
nomeCliente=input('Digite o seu nome: ')
# card = escolhaCardapio()

