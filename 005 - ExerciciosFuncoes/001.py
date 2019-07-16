def num(n):
    lista = []
    for i in range(1,n+1):
        lista.append(str(i))
        for j in range(1):
            print(' '.join(lista))
    return n

num(n = int(input('N: ')))

