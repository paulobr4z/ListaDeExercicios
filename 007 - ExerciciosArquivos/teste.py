'''
Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que
adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa
terá uma lista de palavras lidas de um arquivo texto e escolherá uma
aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra.
Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou
ou perdeu o jogo.
'''
import random

lista=['gato','cachorro','casa']
palavra=[]

r = random.randint(0,2)
for i in lista[r]:
    palavra.append(i)
random.shuffle(palavra)

print(' '.join(palavra))
palpite = input('Qual a palavra sorteada: ')

cont = 0

while palpite != lista[r]:
    if cont == 5:
        break
    cont += 1
    print(f'Você errou! Você tem mais {6-cont} tentativas')
    palpite = input('Qual a palavra sorteada: ')
if cont < 5:
    print('Voce acertou!')
elif palpite == lista[r]:
    print('Você acertou!')
else:
    print('Voce perdeu!')
