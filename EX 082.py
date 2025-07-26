lista = []
listap = []
listai = []
continuar = 'S'

while continuar == 'S':
    n = int(input('Digite um número: '))
    lista.append(n)

    if n % 2 == 0:
        listap.append(n)

    else:
        listai.append(n)

    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

    while continuar not in 'SsNn':
        continuar = str(input('Valor Invalido, Deseja continuar? [S/N]: ')).strip().upper()[0]

else:
    print(lista)
    print(listap)
    print(listai)