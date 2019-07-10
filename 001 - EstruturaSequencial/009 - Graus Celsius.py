'''
Faça um Programa que peça a temperatura em graus Farenheit, transforme e
mostre a temperatura em graus Celsius.
C = (5 * (F-32) / 9).
'''
F = float(input('Quanto graus Farenheit? '))

C = (5 * (F-32) / 9)

print('%.2f graus Farenheit são %.2f graus Celsius'%(F, C))
