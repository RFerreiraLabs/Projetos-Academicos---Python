lista = [[], []]


for c in range (1,8):
    valor = int(input(f'Digite o {c}° Valor: '))
    c += 1
    if valor % 2 == 0:
        lista[0].append(valor)


    if valor % 2 == 1:
        lista[1].append(valor)

lista[0].sort()
lista[1].sort()


print(lista)

