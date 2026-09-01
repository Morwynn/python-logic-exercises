preco = float(input('Digite o preço do produto: '))
formas_pagamento = input('Qual a forma de pagamento: ').lower()
desconto = preco * 10 / 100
preco_final = preco - desconto

if formas_pagamento == "pix":
    print('R$', preco_final)
elif formas_pagamento == "dinheiro":
    print('R$', preco_final)
elif formas_pagamento == "cartao":
    print('R$', preco)
else:
    print('Forma de pagamento invalida.')