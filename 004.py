#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

algo = input('Digite algo: ')

print('o tipo primitivo desse algo é', type(algo))
print('o algo possui apenas espaços?', algo.isspace())
print('é somente um número?', algo.isnumeric())
print('é apenas alfabético?', algo.isalpha())
print('é numérico e alfabético?', algo.isalnum())
print('está em maiusculo?', algo.isupper())
print('está em minusculo?', algo.islower())
print('está capitalisado?', algo.istitle())
