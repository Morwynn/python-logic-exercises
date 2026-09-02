nome_produto = input('Qual o produto?: ')
quantidade = int(input('Qual a quantidade comprada?: '))
preco_produto = float(input('Qual o valor do produto?: '))
valor_total_compra = quantidade * preco_produto

#var. descontos

desconto_5 = valor_total_compra * 5 / 100
desconto_10 = valor_total_compra * 10 / 100
desconto_15 = valor_total_compra * 15 / 100

print('Produto:', nome_produto)
print('Quantidade:', quantidade)
print('Preço do produto: R$', preco_produto)
print('Valor da compra: R$', valor_total_compra)


if valor_total_compra <= 100:
    print('Sua compra não tem desconto')
elif valor_total_compra < 500:
    print('Sua porcentagem de desconto é de 5%')
    print('Valor descontador é de: R$', desconto_5)
    print('Valor total de descont é de: R$', valor_total_compra - desconto_5)
elif valor_total_compra < 1000:
    print('Sua porcentagem de desconto é de 10%')
    print('Valor descontador é de: R$', desconto_10)
    print('Valor total de descont é de: R$', valor_total_compra - desconto_10)
else:
    print('Sua porcentagem de desconto é de 15%')
    print('Valor descontado é de: R$', desconto_15)
    print('Valor total de desconto é de: R$', valor_total_compra - desconto_15)