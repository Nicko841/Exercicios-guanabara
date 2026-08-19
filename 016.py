#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

n = float(input('Digite um número qualquer: '))
inteiro = int(n // 1)
print('O numero digitado foi {} e sua porção inteira é {}.'.format(n, inteiro))
