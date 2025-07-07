from datetime import date

ano = int(input('que ano voce quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('o ano {} não é bissexto'.format(ano))



'''ano = input('Digite um ano: ')

while not ano.isdigit():
    ano = input('Digite um valor válido')

ano = int(ano)

if (ano % 4 == 0 and  ano % 100 != 0) or (ano % 400 == 0):
    print('o ano de {} é bissexto'.format(ano))

else:
    print('o ano de {} não é bissexto'.format(ano))'''

