name = input('Type a name: ')
username_nonpermited = 'abacaxi', 'feira', 'pastel'

if name == '':
    print('Acesso negado.')
else:
    age = int(input('Type a age: '))

    if age < 18:
        print('Acesso negado')
    else:
        desired_username = input('Type a Username: ').lower()

        if desired_username in username_nonpermited:
            print('Acesso negado')
        elif ' ' in desired_username:
            print('Acesso negado')
        elif desired_username == '':
            print('Acesso negado')
        else:
            print('Acesso permitido')
    