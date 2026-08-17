#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

inicial = float(input('digite seu salário atual: R$'))
final = inicial + ((inicial / 100) * 15)
print('Após um aumento de 15%, seu novo salário é: R${:.2f}'.format(final))
