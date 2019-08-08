'''
Faça um Programa que leia três números e mostre o maior deles.
'''
EX: 01

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


EX: 02

lista=[]

lista.append(n1)
lista.append(n2)
lista.append(n3)

print('menor:',min(lista))
print('maior:',max(lista))
