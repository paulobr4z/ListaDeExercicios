'''
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene
num vetor a média de cada aluno, imprima o número de alunos com média maior
ou igual a 7.0.
'''
lista = []
cont = 0

for i in range(1,11):
    sublista = []
    lista.append(sublista)
    print(f'\nAluno {i}')
    for j in range(1,5):
        nota = float(input(f'Digite a nota {j} de 4: '))
        sublista.append(nota)
        soma = sum(sublista)
        media = soma /4
    if media >= 7:
        cont += 1
        print(f'Média = {media}')
    else:
        print('O aluno não atingiu a média')
print(f'\nN° de alunos com média maior ou iguail a 7 = {cont}')
