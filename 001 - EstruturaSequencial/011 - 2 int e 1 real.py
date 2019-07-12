'''
Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
'''

i1 = int(input('Digite 1° número inteiro: '))
i2 = int(input('Digite 2° número inteiro: '))
r1 = float(input('Digite 1° número real: '))

resp1 = (i1 * 2) * (i2 / 2)
resp2 = (i1 * 3) + r1
resp3 = r1 ** 3

print(f'Resposta 1 = {resp1}')
print(f'Resposta 2 = {resp2}')
print(f'Resposta 3 = {resp3}')
