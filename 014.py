#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

C = float(input('Digite uma temperatura em graus celsius: '))
F = (C * 9/5) + 32
print('Essa temperatura equivale a {:.2f} graus Fahrenheit'.format(F))
