'''
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma,
a multiplicação e os números.
'''
lista = []
prod = 1

for i in range(1,6):
    lista.append(i)
    soma  = sum(lista)
    prod *= i
print(f'Lista = {lista}')
print(f'Soma = {soma}')
print(f'Mult = {prod}')
