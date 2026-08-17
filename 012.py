#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Digite o valor do produto: R$'))
valor = p - ((p / 100) * 5)
print('Após 5% de desconto, o valor final é de R${:.2f}'.format(valor))
