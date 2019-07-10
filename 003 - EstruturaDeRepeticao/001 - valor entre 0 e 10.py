'''
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso
o valor seja inválido e continue pedindo até que o usuário informe um valor
válido.
'''
n = int(input('Digite um numero entre 0 e 10: '))

while n > 10:
    n = int(input(f'{n} valor inválido: '))
print(f'{n} valor aceito, está entre 0 e 10')
