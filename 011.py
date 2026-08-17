#Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

l1 = float(input('Largura da parede em metros: '))
l2 = float(input('Altura da parede em metros: '))
area = l1 * l2
tinta = area / 2
print('sua parede tem uma área de {}'.format(area))
print('para pintala será necessário {} litros de tinta'.format(tinta))
