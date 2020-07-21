import os
from time import sleep
#                 FUNÇÃO PARA ESCOLHER O CARDAPIO - TAMBÉM PRIMEIRA TELA
def escolhaCardapio():
    #global card
    flag = 1
    while flag != 0:
        os.system('cls')
        print("ESCOLHA SEU CARDÁPIO\n")
        print("> Digite 1 para abrir o caradápio de Sorvete")
        print("> Digite 2 para abrir o cardápio de Açai")
        print("> Digite 0 Finalizar pedido.")
        card = int(input("Escolha: "))
        if card > 2 or card < 0:
            print('Valor inválido, escolha outra opção.')
            sleep(1)
        elif card == 0:
            print("FIM DO PEDIDO!!!")  # tem que chamar a função aqui que calcula tudo
            sleep(1)
            flag = 0
        else:
            flag = 0      
    return card


#                   FUNÇAO QUE ESCOLHE O TAMANHO DO SORVETE/ACAI (CHAMA FUNCAO MENU SORVETE/ACAI)
def tamanhosPreco():
    os.system('cls')
    print('DIGITE O NÚMERO CORRESPONDENTE: ')
    print('1 - Pequeno 200ml: 4,00 R$ ')
    print('2 - Medio 400ml: 7,00 R$')
    print('3 - Grande 600ml: 10,00 R$')
    print('0 - VOLTAR')
    condicao = 1
    while condicao != 0:
        tam = int(input('Escolha o tamanho: '))
        if tam > 3 or tam < 0:
            print('Opção inválida.')
        else:
            condicao = 0
    return tam
            
def cardSorvete(tam):  # Após escolher o sabor o pedido do usuário vai par o "carrinho com o sabor e o preço"
    sabor = ('Chocolate', 'Baunilha', 'Flocos', 'Morango')
    flag = 1
    pedidoCliente = []
    while flag != 0:
        limparTela()
        print("Nossos sabores são: ")
        for i in range(len(sabor)):
            print(f'{i + 1} - {sabor[i]}')
        
        if tam == 1:
            opcao = int(input('Escolha seu sabor: '))
            if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
                print('Opção inválida')
            else:
                pedidoCliente.append(sabor[opcao - 1])
                pedidoCliente.append('Pequeno: 4,00R$')
                print(pedidoCliente)
                flag = 0
        elif tam == 2:
            i = 0
            while i < 2:
                opcao = int(input(f'Escolha o {i + 1}º sabor: '))
                if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
                    print('Opção inválida')
                else:
                    pedidoCliente.append(sabor[opcao - 1])
                    print(pedidoCliente)
                    i += 1
            pedidoCliente.append('Medio: 7,00R$')
            flag = 0
        else:
            i = 0
            while i < 3:
                opcao = int(input(f'Escolha o {i + 1}º sabor: '))
                if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
                    print('Opção inválida')
                else:
                    pedidoCliente.append(sabor[opcao - 1])
                    print(pedidoCliente)
                    i += 1
            pedidoCliente.append('Grande: 10,00R$') 
            flag = 0
        sleep(1.5)        
    return pedidoCliente
   
 
def cardAcai(tam):  # Após escolher o sabor o pedido do usuário vai par o "carrinho com o sabor e o preço"
    complementos =('Catanha','Amendoim','Banana','Achocolatado','Leite em pó')
    print("Nossos complementos são: {}".format(complementos))

    seusComplementos = []
    print("Você tem direito a {} complemento(s)".format(tam))
    while len(seusComplementos) < tam:
 
        print("Escolha seu {}º complemento.:(escreva) ".format(len(seusComplementos) + 1))
        nomeDoComp = input()
        seusComplementos.append(nomeDoComp)
        
    print("Seus complementos foram: {}".format(seusComplementos))

''' 
def nota(tam):
    print(nomeCliente)
    print('O preço a ser pago é R${:.2f}.'.format(preco))
    cpfnota=input('Deseja CPF na nota? S/N').upper
    if cpfnota == 'S':
      print('arroz')
      #função do cpf
    elif cpfnota == 'N':
      valorpago = float(input('Digite o valor pago: '))
      if valorpago == preco:
            print('PEDIDO ENCERRADO')
      elif valorpago != preco:
        if valorpago > preco:
              troco = valorpago-preco
              print(troco)
        else:
              falta = preco-valorpago
              print(falta)
'''

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


def limparTela():
    os.system('cls')

def mostrarCarrinho(lista):
    limparTela()
    for i in lista:
        lista1 = i[:]
        print(f'Sorvete {i[-1]}')
        lista1.pop(-1)
        print('Sabor(es): ')
        for x in lista1:
            print(x, end=' ')
        print()
    input()


'''
PARAMOS NESSA FUNÇAO
'''
print('BEM VINDO À SORVEETERIA PY \n')
nomeCliente=input("Digite seu nome para começarmos: ")
flag = 1
carrinho = []
while flag != 0:
    pedido = escolhaCardapio()
    if pedido == 1: # Sorvete 
        tamanho = tamanhosPreco()
        if tamanho == 0:
            pass
        else: 
            carrinho.append(cardSorvete(tamanho))
            #print(carrinho[0])
            mostrarCarrinho(carrinho)
            sleep(1)
    elif pedido == 2: # Açai
        tamanho = tamanhosPreco()
        if tamanho == 0:
            pass
        else:
            carrinho.append(cardAcai(tamanho))
            #print(carrinho[0])
            mostrarCarrinho(carrinho)
            sleep(1)
    else:
            #Chamar função nota
        flag = 0
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

