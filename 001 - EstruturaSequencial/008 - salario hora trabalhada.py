'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
'''
valor_hora = int(input('Quanto vc ganha por hora: '))
hora_trabalhada = int(input('Quantas horas vc tranbalha por mês? '))
salario = valor_hora * hora_trabalhada
print(f'Seu salario é: R$ {salario} reais')
