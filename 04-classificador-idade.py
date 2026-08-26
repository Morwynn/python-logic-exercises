try:

    idade = int(input('Digite uma idade: '))

    if idade <= 12:
        print('Esta pessoa é uma criança.')
    elif idade <= 17:
        print('Está pessoa é um adolescente.')
    elif idade <= 59:
        print('Esta pessoa é um adulto')
    else:
        print('Esta pessoa é um idoso.')

except: ValueError
print('Digite uma idade de forma numérica.')