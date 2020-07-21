import os
 
def limparTela():
  os.system('cls')

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
            #nota()
            break
        else:
            print('Valor inválido, escolha outra opção.')
 
 
def cardSorvete(tam):  # Após escolher o sabor o pedido do usuário vai par o "carrinho com o sabor e o preço"
    sabores = ('Chocolate','Baunilha','Flocos','Morango')
    print("Nossos sabores são: {}".format(sabores))

    seusSabores = []
    while len(seusSabores) < tam:
        print("Escolha seu {}º sabor.:(escreva) ".format(len(seusSabores) + 1))
        nomeDoSabor = input()
        seusSabores.append(nomeDoSabor)
    print("Seus sabores foram: {}".format(seusSabores))
    
 
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


 
#                   FUNÇAO QUE ESCOLHE O TAMANHO DO SORVETE/ACAI (CHAMA FUNCAO MENU SORVETE/ACAI)
def tamanhosPreco(opt):
    print('DIGITE O NÚMERO CORRESPONDENTE: ')
    print('1 - PEQUENO = 200ml = 4,00 R$ ')
    print('2 - MEDIO = 400ml = 7,00 R$')
    print('3 - GRANDE = 600ml = 10,00 R$')
    print('0 - VOLTAR')
    condicao = 1
    global preco
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
print('BEM VINDO À SORVETERIA PY \n')
nomeCliente=input("Digite seu nome para começarmos: ")
escolhaCardapio()
print(nomeCliente)
#nota()

