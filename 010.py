#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

n = float(input('Digite o valor financeiro disponivel: R$'))
dol = n / 5.2 #valor de 17/08/2026
print('Com o valor disponivel é possivel adiquirir {:.2f} dólares.'.format(dol))
