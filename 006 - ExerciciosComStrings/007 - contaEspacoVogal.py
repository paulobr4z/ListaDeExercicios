'''
Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário
(incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u.
'''
s = input('Digite uma frase: ')

s = s.lower()

emBranco = s.count(' ')
a = s.count('a')
e = s.count('e')
i = s.count('i')
o = s.count('o')
u = s.count('u')
soma = a+e+i+o+u

print(f'Na frase existe {emBranco} espaços em branco.')
print(f'Na frase existe {soma} vogais.')
