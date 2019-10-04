'''
Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''
n1 = input('Digite o 1 número: ')
n2 = input('Digite o 2 número: ')
n3 = input('Digite o 3 número: ')

if n1 < n2 and n2 < n3:
    print(n1,n2,n3)
elif n1 < n3 and n3 < n2:
    print(n1,n3,n2)
elif n2 < n1 and n1 < n3:
    print(n2,n1,n3)
elif n2 < n3 and n3 < n1:
    print(n2,n3,n1)
elif n3 < n1 and n1 < n2:
    print(n3,n1,n2)
elif n3 < n2 and n2 < n1:
    print(n3,n2,n1)
