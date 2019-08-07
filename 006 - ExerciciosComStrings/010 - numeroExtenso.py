'''
Número por extenso. Escreva um programa que solicite ao usuário a digitação de
um número até 99 e imprima-o na tela por extenso.
'''
a=['um','dois','três','quatro','cinco',
   'seis','sete','oito','nove']
b=['onze','doze','treze','quatorze','quinze',
   'dezeseis','dezesete','dezoito','dezenove']
c=['vinte','trinta','quarenta','cinquenta','sessenta',
   'setenta','oitenta','noventa']

num = int(input('Digite um número entre 1 e 99: '))

while num < 1 or num > 99:
    print('Número inválido. Tente novamente!')
    num = int(input('Digite um número entre 1 e 99: '))
    
if num // 10 == 0:
    print(f'{a[num-1]}')
elif num // 10 == 1:
    print(f'{b[(num%10)-1]}')
elif num // 10 > 1 and num % 10 > 0:
    print(f'{c[(num // 10)-2]} e {a[(num%10)-1]}')
elif num // 10 > 1:
    print(f'{c[(num // 10)-2]}')
