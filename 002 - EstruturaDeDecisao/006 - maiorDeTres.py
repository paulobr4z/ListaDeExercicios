'''
Faça um Programa que leia três números e mostre o maior deles.
'''

n1 = int(input('Digite o 1 número: '))
n2 = int(input('Digite a 2 número: '))
n3 = int(input('Digite a 3 número: '))

maior = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
   
print(maior)

ex2

n1 = int(input('Digite o 1 número: '))
n2 = int(input('Digite a 2 número: '))
n3 = int(input('Digite a 3 número: '))

if n1 > n2 and n1 > n3:
    print(n1)
elif n2 > n1 and n1 > n3:
    print(n2)
elif n3 > n1 and n3 > n2:
    print(n3)
