'''
Faça um Programa que peça a temperatura em graus Farenheit, transforme e
mostre a temperatura em graus Celsius.
C = (5 * (F-32) / 9).
'''
f = float(input('Quanto graus Farenheit? '))
c = (5 * (f-32) / 9)
print(f'{f:.2f} graus Farenheit são {c:.2f} graus Celsius')
