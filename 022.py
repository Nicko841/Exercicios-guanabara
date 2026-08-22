#Crie um programa que leia o nome completo de uma pessoa e mostre: 
#
#    O nome com todas as letras maiúsculas e minúsculas.
#    Quantas letras ao todo (sem considerar espaços).
#    Quantas letras tem o primeiro nome.

nome = input('Digite seu nome: ')
nome = nome.strip()
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
lista = nome.split()
letras = 0
n = 0
while n < len(lista):
    letras = letras + len(lista[n])
    n = n + 1
print('Seu nome tem {} letras no total'.format(letras))
print('Seu primeiro nome tem {} letras'.format(len(lista[0])))
