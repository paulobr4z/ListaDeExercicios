print('Qual o melhor Sistema Operacional para uso em servidores?')
print('\nAs possíveis respostas são:\n')

sistemas = ['1- Windows Server','2- Unix','3- Linux','4- Netware','5- Mac OS','6- Outro']

for i in sistemas:
    print(i)

lista = []

v = int(input('\nDigite seu voto: '))

while v != 0:
    if v <= 6:
        lista.append(v)
        v = int(input('Digite seu voto: '))
    else:
        print('Digite um numero de 1 a 6 ou 0 para encerrar a votação')
        v = int(input('Digite seu voto: '))
print(lista)

h1,h2,h3 = 'Sistema Operacional','Votos','%'
print(f'{h1:25}{h2:8}{h3:3}')
print('-------------------      -----   ---')

for i in sistemas:
    print(f'{i:}')
