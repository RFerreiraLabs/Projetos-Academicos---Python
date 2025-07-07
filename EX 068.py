from random import randint

cont = 0

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    tipo = str(input('PAR OU IMPAR? [P/I]: ')).strip().upper()[0]
    while tipo not in "PI":
        tipo = str(input('PAR OU IMPAR? [P/I]: '))

    if tipo == 'P':
        print(f'Voce jogou {jogador} e o computador {computador}. Total de {total}')
        if total % 2 == 0:
            print('VOCE VENCEU')
            cont += 1
        else:
            print('VOCE PERDEU')
            break

    elif tipo == 'I':
        print(f'Voce jogou {jogador} e o computador {computador}. Total de {total}')
        if total % 2 == 1:
            print('VOCE VENCEU')
            cont += 1
        else:
            print('VOCE PERDEU')
            break
    print('VAMOS JOGAR NOVAMENTE...')
print(f'GAMER OVER! Voce venceu {cont} vezes')







