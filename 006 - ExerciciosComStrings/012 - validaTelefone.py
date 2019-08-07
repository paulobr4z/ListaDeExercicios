'''
Valida e corrige número de telefone. Faça um programa que leia um número de
telefone, e corrija o número no caso deste conter somente 7 dígitos,
acrescentando o '3' na frente. O usuário pode informar o número com ou sem o
traço separador.
'''
lista=[]

while len(lista) < 7 or len(lista) > 8:
    tel = input('Digite o seu número de telefone: ')

    for i in tel:
        if i != '-' and i != ' ':
            lista.append(i)
    
    if len(lista) < 7 or len(lista) > 8:
        print('Número de telefone invalido!')
        lista.clear()

print('Valida e corrige número de telefone.')
a = ''.join(lista)

if len(lista) == 7:
    print(f'Telefone: {a[0:3]}-{a[3:7]}')
    print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
    print(f'Telefone corrigido sem formatação: 3{a}')
    print(f'Telefone corrigido com formatação: 3{a[0:3]}-{a[3:7]}')
elif len(lista) == 8:
    print(f'Telefone corrigido com formatação: {a[0:4]}-{a[4:8]}')
elif len(lista) < 7 or len(lista) > 8:
    print('Número de telefone invalido!')
