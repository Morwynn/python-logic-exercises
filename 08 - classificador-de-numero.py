try:

    inteiro = int(input("Digite um numero inteiro: "))

    if inteiro > 0:
        print ('Seu numero é positivo')
    elif inteiro < 0:
        print('Seu numero é negativo')
    else:
        print('Seu numero é zero')

    if inteiro % 2 == 0:
        print ('Seu numero é par')
    else:
        print ('Seu numero é impar')
        
    if inteiro % 5 == 0:
        print('Seu numero é multiplo de 5')
    else: 
        print('Seu numero não é multiplo de 5')
    
except ValueError:
    print('Digite um numero.')