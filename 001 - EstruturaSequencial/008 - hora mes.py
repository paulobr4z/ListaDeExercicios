'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
'''
vh = int(input('Quanto vc ganha por hora? '))
nh = int(input('Quantas horas vc tranbalha por mês? '))

salario = vh * nh

print('Seu salario é: R$ %i reais'%salario)
