'''
Faça um programa que receba a temperatura média de cada mês do ano e
armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e
mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram
(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
'''
import random

lista = []
meses = ['jan','fev','mar','abr','mai','jun','jul','ago','sete','out','nov','dez']

for i in range(1,13):
    temp = random.randint(0,42)
    print(f'Qual a temp media desse mês {i} de 12: {temp}')
    lista.append(temp)

print(' ')
media = sum(lista)/12
print(f'Média anual = {media:.2f} graus\n')
print('Meses com temp maior q a média anual')

for i in range(len(lista)):
    if lista[i] > media:
        print(meses[i], end=' ')
