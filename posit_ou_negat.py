try: # código que pode dar erro
    numero = int(input("Digite um numero: ")
                       )

    if numero > 0:
        print('Seu numero é positivo.'
              )
    elif numero < 0:
        print('Seu numero é negativo.'
              )
    else:
        print('Zero'
              )

except: # o que fazer se der erro
    print ('Não é um numero.')




