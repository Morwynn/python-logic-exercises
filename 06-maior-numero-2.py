numero_1 = int(input('1° Numero: '))
numero_2 = int(input('2° Numero: '))
numero_3 = int(input('3° Numero: '))

if numero_1 >= numero_2 and numero_1 >= numero_3:
    print(f'O maior numero é {numero_1}.')
elif numero_2 >= numero_1 and numero_2 >= numero_3:
    print(f'O maior numero é {numero_2}.')
elif numero_3 >= numero_2 and numero_3 >= numero_1:
    print(f'O maior numero é {numero_3}.')
