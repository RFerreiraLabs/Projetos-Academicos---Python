from time import sleep

def contador():
    print('-=' * 20)
    print('Contagem de 1 até 10 de 1 em 1')
    for contador in range (1,11, 1):
        print(contador,end=' ')
    print('FIM')

    print('-=' * 20)
    print('Contagem de 10 até 0 de 2 em 2')
    for contador in range (10, -1, -2):
       print(contador,end=' ')
    print('FIM')
    print('-=' * 20)

    print('Agora é sua vez de personalizar a contagem!')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    print('-=' * 20)

    if passo == 0:
        passo = 1

    if passo > 0 and fim > inicio:
        for contador in range(inicio, fim + 1, passo):
            print(contador,end=' ')
        print('FIM')

    elif fim < inicio:
        for contador in range(inicio, fim - 1, passo * -1):
            print(contador,end=' ')
        print('FIM')

contador()
