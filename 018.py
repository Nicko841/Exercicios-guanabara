#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
ang = float(input('Digite um angulo qualquer em graus: '))
rad = math.radians(ang)
senolegal = math.sin(rad)
cosenolegal = math.cos(rad)
tangentelegal = math.tan(rad)
print('o seno do angulo é {}'.format(senolegal))
print('o cosseno do angulo é {}'.format(cosenolegal))
print('a tangente do angulo é {}'.format(tangentelegal))
