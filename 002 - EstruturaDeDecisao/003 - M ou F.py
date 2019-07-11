'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''
l = input('digite uma letra: ')

if l == 'M' or l == 'm':
    print(f'{l} - Masculino')
elif l == 'F' or l == 'f':
    print(f'{l} - Feminino')
else:
    print(f'Sexo Inválido')
