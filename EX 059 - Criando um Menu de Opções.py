from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:

    print('''    [1] somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do programa''')
    opção = int(input('Qual é a sua opção?: '))

    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1,n2, soma))
    elif opção == 2:
        mult = n1 * n2
        print('A multiplicação de {} * {} é {}'.format(n1,n2, mult))

    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('entre {} e {} o maior valor é {}'.format(n1,n2, maior))

    elif opção == 4:
        print('Informe os numeros novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    elif opção == 5:
        print('Finalizando...')

    else:
        print('Opção inválida, tente novamente! ')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa')
