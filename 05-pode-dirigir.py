idade = int(input('Qual a sua idade?: '))
tem_carta = input('Tem carteira de motorista?: ').lower()

if idade >= 18 and tem_carta == 'sim':
    print ('Você pode dirigir.')
else:
    print('Você não pode dirigir')
    

