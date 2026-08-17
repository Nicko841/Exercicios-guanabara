#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

d = int(input('A quantos dias o carro foi alugado? Digite: '))
km = float(input('Quantos kilometros foram percorridos? Digite: '))
valor = (d * 60) + (km * 0.15)
print('O total a se pagar pelo aluguel do carro é de R${:.2f}'.format(valor))
