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

#ex2
def num(n):
    lista = []
    for i in range(1,n+1):
        lista.append(str(i))
        for j in range(1):
            print(' '.join(lista))
    return n

num(n = int(input('N: ')))

