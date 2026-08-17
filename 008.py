#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

valor = float(input('Digite um valor em metros para ser convertido: '))
c = valor * 100
mm = c * 10
print('{} Metros equivale a: {} centímetros, ou, {} milímetros'.format(valor, c, mm))
