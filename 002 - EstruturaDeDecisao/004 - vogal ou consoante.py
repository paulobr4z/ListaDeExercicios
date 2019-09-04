'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''
l = input('Digite uma letra: ')

if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u' or \
   l == 'A' or l == 'E' or l == 'I' or l == 'O' or l == 'U':
    print(f'{l} é vogal')
else:
    print(f'{l} é consoante')

#ex2

vogal = ['a','e','i','o','u']

letra = input('Digite uma letra: ').lower()

if letra not in vogal:
  print(f'{letra} é consoante')
else:
  print(f'{letra} é vogal')
