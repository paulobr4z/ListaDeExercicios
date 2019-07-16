'''
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
'''
#ex1
def num(n):
    for i in range(1,n+1):
        print(str(i)*i)
    return n

num(n = int(input('N: ')))

#ex

def num2(n):
    lista = []
    for i in range(1,n+1):
        lista.append(str(i))
        print(' '.join(lista[int(i-1)]*i))
num2(n = int(input('N: ')))
