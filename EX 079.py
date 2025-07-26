
lista = []
continuar = 'S'


while continuar == 'S':
    valor = int(input('Digite um valor: '))

    if valor in lista:

        print('valor duplicado, nao vou adicionar')
    else:
        lista.append(valor)
    print(lista)


    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]

    while continuar not in 'SsNn':
        continuar = str(input(' GUI NOOB, Deseja continuar? [S/N]')).strip().upper()[0]

lista.sort()
print('-=' * 40)
print(f'Voce digitou os valores {lista}')










