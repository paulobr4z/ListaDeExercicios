'''
Data com mês por extenso. Construa uma função que receba uma data no formato
DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA.
Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
'''
meses = ['janeiro','fevereiro','março','abril',
         'maio','junho','julho','agosto','setembro',
         'outubro','novembro','dezembro']


def dataExtenso():
    data = input('Digite uma data (xx/xx/xxx): ')
    a = data.split('/')
    b = int(data[1])    
    c = data.replace(f'/{a[1]}/',f' de {meses[b-1]} de ')
    print(c)
dataExtenso()
