'''
Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo
delas seguido do seu comprimento. Informe também se as duas strings possuem o
mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
'''
s1 = input('String 01: ')
s2 = input('String 02: ')

print(f'Tamanho de {s1}: {len(s1)} caracteres.')
print(f'Tamanho de {s2}: {len(s2)} caracteres.')

if len(s1) == len(s2):
    print('As duas strings são de tamanhos diferentes.')
else:
    print('As duas strings possuem conteúdo diferente.')
