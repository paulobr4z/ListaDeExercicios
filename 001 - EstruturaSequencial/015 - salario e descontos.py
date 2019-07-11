'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''
valor_hora = 16 #int(input('Quanto vc ganha por hora: '))
num_hora = 80#int(input('Quantas hora vc trabalha no mes: '))
salario = valor_hora * num_hora
ir = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05
salario_liq = salario - ir - inss - sindicato

print(f'+ Salário  Bruto   R$ {salario:8.2f} reais')
print(f'- IR (11%)         R$ {ir:8.2f} reais')
print(f'- INSS (8%)        R$ {inss:8.2f} reais')
print(f'- Sindicato (5%)   R$ {sindicato:8.2f} reais')
print(f'= Salário Liquido  R$ {salario_liq:8.2f} reais')
