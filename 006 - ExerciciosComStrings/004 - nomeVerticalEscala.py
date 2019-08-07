'''
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar
o nome em formato de escada.
'''
nome = input('Digite seu nome: ')

for i in range(len(nome)):
    print(nome[0:1+i])
