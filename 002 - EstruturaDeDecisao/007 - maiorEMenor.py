'''
Faça um Programa que leia três números e mostre o maior e o menor deles.
'''

n1 = int(input('Digite o 1 número: '))
n2 = int(input('Digite a 2 número: '))
n3 = int(input('Digite a 3 número: '))

#EX: 01

maior = n1
menor = n1

if maior < n2:
	maior = n2
if maior < n3: 
	maior = n3
if menor > n2:
	menor = n2
if menor > n3:
	menor = n3

print (f'Menor: {menor})
print (f'Maior: {maior})


#EX: 02
num = []

for i in range(3):
  n = input(f'Digite o {i+1} número: ')
  num.append(n)
       
print('menor:',min(num))
print('maior:',max(num))
