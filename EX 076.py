listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, "Estojo",
            25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila',
            120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-' * 56)
print(' ' * 18, 'LISTAGEM DE PREÇOS', ' ' * 10)
print('-' * 56)
for indice in range (len(listagem)):

    if indice % 2 == 0:
        produto = (listagem[indice])
    if indice % 2 == 1:
        preco = (listagem[indice])
        print(f'{produto:.<30}................R$ {preco:>7.2f}')

print('-' * 56)




