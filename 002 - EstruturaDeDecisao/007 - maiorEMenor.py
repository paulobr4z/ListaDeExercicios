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

lista=[]

lista.append(n1)
lista.append(n2)
lista.append(n3)

print('menor:',min(lista))
print('maior:',max(lista))
