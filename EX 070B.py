while True:
    produto = str(input('NOME DO PRODUTO: '))
    preco = float(input('PREÇO: R$  '))

    resp = ' '
    while resp not in 'SN':
        resp = str(input('QUER CONTINUAR [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
