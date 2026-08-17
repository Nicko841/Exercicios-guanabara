#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
Dn = n * 2
Tn = n * 3
Rn = n ** (1/2)
print('Dobro: {} -///- Triplo: {} -///- Raiz quadrada: {}'.format(Dn,Tn,Rn))
