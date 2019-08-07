'''
Data por extenso. Faça um programa que solicite a data de nascimento
(dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.
'''
meses = ['janeiro','fevereito','março','abril',
         'maio','junho','julho','agosto','setembro',
         'outubro','novembro','dezembro']

dn = input('Digite sua data de nascimento: ')
a = dn.split('/')
b = (int(a[1]))
dn = dn.replace(f'/{a[1]}/', f' de {meses[b-1]} de ')
print(f'Você nasceu em: {dn}')
