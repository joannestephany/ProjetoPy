import os
from time import sleep
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
    while condicao != 0:
        tam = int(input('Escolha o tamanho: '))
        if tam != 1 and tam != 2 and tam != 3 and tam != 0:
            print('Opção inválida.')
        else:
            return tam
            



def cardSorvete(tam):  # Após escolher o sabor o pedido do usuário vai par o "carrinho com o sabor e o preço"
    sabor = ('Chocolate', 'Baunilha', 'Flocos', 'Morango')
    print("Nossos sabores são: ")
    for i in range(len(sabor)):
        print(f'{i + 1} - {sabor[i]}')
    seusSabores = []
    if tam == 1:
        opcao = int(input('Escolha seu sabor: '))
        if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
            print('Opção inválida')
        else:
            seusSabores.append(sabor[opcao - 1])
            print(seusSabores)
            sleep(2)
    elif tam == 2:
        for i in range(2):
            opcao = int(input(f'Escolha o {i + 1}º sabor: '))
            seusSabores.append(opcao - 1)
            print(seusSabores)
    else:
        for i in range(3):
            opcao = int(input(f'Escolha o {i + 1}º sabor: '))
            seusSabores.append(opcao - 1)
            print(seusSabores)
    return seusSabores
   
   
    '''
    while len(seusSabores) < tam:
        print("Escolha seu {}º sabor.:(escreva) ".format(len(seusSabores) + 1))
        nomeDoSabor = input()
        seusSabores.append(nomeDoSabor)
    print("Seus sabores foram: {}".format(seusSabores))
    '''
 
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




'''
PARAMOS NESSA FUNÇAO
'''
print('BEM VINDO À SORVEETERIA PY \n')
nomeCliente=input("Digite seu nome para começarmos: ")
pedido = 1
carrinho = []
while pedido != 0:
    pedido = escolhaCardapio()
    if pedido == 1: # Sorvete 
        tamanho = tamanhosPreco()
        if tamanho == 0:
            pass
        else: 
            cardSorvete(tamanho)
    elif pedido == 2: # Açai
        tamanho = tamanhosPreco()
        if tamanho == 0:
            pass
        else: 
            cardAcai(tamanho)
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

