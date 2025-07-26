lista = []
cont = 0

for c in range (0,5):
    n = int(input('Digite um valor: '))

    if c == 0: #aqui o comando automaticamente insere o primeiro numero na lista
        # com o comando .append
        lista.append(n)

    elif n > lista[len(lista)-1]: # Nessa parte o programa verifica se o novo numero
        # inserido é maior que o ultimo, e se assim o for, irá pro final com o comando
        # append
        # note que lista procura pelo ultimo indice (-1) na lista
        lista.append(n)

    else:
        pos = 0

        while pos < len(lista): #olha numero por numero dentro da lista utilizando o contador pos
            if n <= lista[pos]:
                lista.insert(pos,n)
                break

            pos +=1

print('-=' * 30)
print(f'Os valores digitados em ordem foram: {lista}')









