'''
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''
lista = []

for i in range(1,5):
    n = float(input(f'Digite {i} nota de 4: '))
    lista.append(n)
soma = sum(lista)
media = soma/4
print(f'Média = {media}')
