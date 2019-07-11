'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a
velocidade de um link de Internet (em Mbps), calcule e informe o tempo
aproximado de download do arquivo usando este link (em minutos).
'''
tamanho_arquivo = 10#int(input('Qual o tamanho do arquivo: '))
velocidade_internet = 1#int(input('Qual a velocidade da internet: '))

tempo_download = tamanho_arquivo * (velocidade_internet / 60)

print(f'{tempo_download // 60} minutos')
print(f'{tempo_download / 60} segundos')
print(f'{tempo_download:.2f}')
