'''
Faça um programa que leia um número indeterminado de valores, correspondentes
a notas, encerrando a entrada de dados quando for informado um valor igual a
-1 (que não deve ser armazenado). Após esta entrada de dados, faça:

Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
'''
lista = []
n = int(input('Digite um número qualquer: '))

while n != -1:
    lista.append(n)
    n = int(input('Digite um número qualquer: '))
    

print(lista)
print(f'Quantidade de valores que foram lidos = {len(lista)}')
print(f'Valores informados: {lista}')
print(f'Valores informados ordem inversa: {sorted(lista, reverse=True)}')
print(f'Soma dos valores: {sum(lista)}')
print(f'Média dos valores: {sum(lista)/len(lista)}')
media = sum(lista)/len(lista)
for i in range(len(lista)):
    if lista[i] > media:
        print('Números acima da média: %i'%lista[i], end=' ')
