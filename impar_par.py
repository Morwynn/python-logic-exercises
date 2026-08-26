try:
    numero = int(input('Digite um numero: '))

    if numero % 2 == 0:
        print ('Numero par')
    else:
        print('Numero impar')
except:ValueError

print('Este caracter não é um numero.')
