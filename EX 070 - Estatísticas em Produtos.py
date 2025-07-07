print('-' * 30)
print(' ' * 5, 'LOJA SUPER BARATAO', ' ' * 5)
print('-' * 30)

resp = 'S'
maisbarato = ' '
cont = 0
nomebarato = ' '
totalcompra = 0
maiorprod = 0

while True:

        while resp not in 'SN':
            resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]

        if resp == 'S':

            produto = str(input('Nome do Produto: ')).strip()
            preco = float(input('Preço: R$ '))
            cont += 1
            resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]

            totalcompra += preco

            if preco > 1000:
                maiorprod += 1

            if cont == 1 or preco < maisbarato:
                maisbarato = preco
                nomebarato = produto


        elif resp == 'N':
            break

print(f' O TOTAL da compra foi R$ {totalcompra} reais')
print(f' Temos {maiorprod} produto custando mais de R$ 1000.00')
print(f' O produto mais barato foi {nomebarato} que custa {maisbarato:.2f} reais')
