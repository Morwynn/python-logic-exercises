
numero_1 = int(input('Digite um numero: ')
               )
numero_2 = int(input('Digite um numero: ')
               )
operacao = input('Qual operação você deseja: '
                 )


if operacao == '+':
    print(numero_1 + numero_2
          )

elif operacao == '-':
    print(numero_1 - numero_2
          )

elif operacao == '*':
    print(numero_1 * numero_2
          )

if operacao == '/':
    if numero_2 == 0:
            print('0 não é divisor'
          )
    else:
            print(numero_1/numero_2
          )