#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

n1 = float(input('Digite o valor de um cateto: '))
n2 = float(input('Digite o valor do outro cateto: '))
hyp = ((n1 ** 2) + (n2 ** 2)) ** (1/2)
print('A hypotenusa desse triangulo retangulo mede {}'.format(hyp))
