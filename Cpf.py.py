# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Sh3Fdk0fp3r2rlKh_CngwIjDdVDC4l07
"""

mult1 = [ 10 , 9 , 8 , 7 , 6 , 5 , 4 , 3 , 2 ]
mult2 = [ 11 , 10 , 9 , 8 , 7 , 6 , 5 , 4 , 3 , 2 ]

soma1 = 0
soma2 = 0

cpf = input ( "Digite seu CPF: " )
#esse for ele vai pegar os 9 primeiros numeros do CPF e fazer uma mutiplicação decrescente de 10 até 2.
for i in range ( 9 ) :
    print ( "CPF" , int ( cpf [ i ] ) , "*" , mult1 [ i ] , "=" , int ( cpf [ i ] ) * mult1 [ i ] )
soma1 = soma1 + (int ( cpf [ i ] ) * mult1 [ i ])
print ( "Soma da 1 verificação: " , mult1 )
verificacao1 = (soma1 * 10) / 11
print ( "O resultado para primeira soma = " , verificacao1 )
#Essa parte ele verifica se o resto é a continuação do cps.
resto1 = (soma1*10) % 11
print ( "O resto da primeira validação é: " , resto1 )

if resto1 == 10:
    resto1 = 0

if resto1 == int(cpf[9]):
    print("verificação confirmada")
else:
    print("CPF invelido.Confira os dados")
#inicio da verificação do ultimo digito do CPF.
for i in range(10):
    print ( "CPF" , int ( cpf [ i ] ) , "*" , mult2 [ i ] , "=" , int ( cpf [ i ] ) * mult2 [ i ] )
    soma2 = soma2 + (int ( cpf [ i ] ) * mult2 [ i ])

    print("O resultado da segunda soma é: ",soma2)
    verificacao2 = (soma2*10)/11
    print("O resultado da segunda soma foi: ", verificacao2)

    resto2 = (soma2*10)%11
if resto2 == 10:
   resto2 = 0

   print( "O resto da segunda verificação foi:" , resto2 )

if resto2 == int(cpf[10]):
    print("Este CPF é valido!")

else:
    print( 'CPF Invalido.Por favor cadestre outro CPF' )