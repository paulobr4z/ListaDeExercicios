'''
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou
negativo.
'''
n = int(input('digite um número: '))

if n > 0:
    print(f'{n} é positivo')
elif n < 0:
    print(f'{n} é negativo')
else:
    print(f'{n} zero')
