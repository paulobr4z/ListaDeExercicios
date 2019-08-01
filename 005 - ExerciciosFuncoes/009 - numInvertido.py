'''
Reverso do número. Faça uma função que retorne o reverso de um número inteiro
informado. Por exemplo: 127 -> 721.
'''

def numInvertido(num):
    inverte = str(num)
    print(f'{inverte[::-1]}')
    
numInvertido(12345)
