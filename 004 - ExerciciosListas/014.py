'''
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre
um crime. As perguntas são:

a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação
sobre a participação da pessoa no crime. Se a pessoa responder positivamente a
2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como
"Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como
"Inocente".
'''
lista = []
perg = ["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?"]
clas = ['inocente','suspeito','cúmplice','Assassino']

for i in range(5):
    r = input(f'{perg[i]}: ')
    if r == 's':
        lista.append(1)
        
s = sum(lista)

if s < 2:
    print(f'Você foi classificado como: {clas[0]}')
elif s == 2:
    print(f'Você foi classificado como: {clas[1]}')
elif s == 3 or s == 4:
    print(f'Você foi classificado como: {clas[2]}')
else:
    print(f'Você foi classificado como: {clas[3]}')
