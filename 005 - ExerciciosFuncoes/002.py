'''
Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro
imprima até a n-ésima linha.
'''

def num(n):
    lista = []
    for i in range(1,n+1):
        lista.append(str(i))
        for j in range(1):
            print(' '.join(lista))
    return n

num(n = int(input('N: ')))

