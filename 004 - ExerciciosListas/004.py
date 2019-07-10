'''
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes
foram lidas. Imprima as consoantes.
'''
vogal = []
conso = []

for i in range(1,11):
    c = input(f'Digite a letra {i} de 10: ')
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        vogal.append(c)
    else:
        conso.append(c)
print(f'{len(conso)} consoantes = {conso}')
