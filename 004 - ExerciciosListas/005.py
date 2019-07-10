'''
Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os três vetores.
'''
par = []
impar = []

for i in range(1,21):
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
print(f'Par = {par}')
print(f'Impar = {impar}')
