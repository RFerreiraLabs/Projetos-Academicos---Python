def ficha(jogador = '', gols = ''):

    if jogador.strip() == '':
        jogador = '<desconhecido>'
        print(f'O jogador {jogador} ', end='')

    else:
        print(f' O jogador {jogador} ', end='')

    if not str(gols).isnumeric():
        gols = 0
        print(f'fez {gols} gol(s) no campeonato')

    else:
        gols = int(gols)
        print(f'fez {gols} gol(s) no campeonato')


#PROGRAMA PRINCIPAL

jogador = str(input('Nome do Jogador: '))
gols = input('Número de Gols: ')

ficha(jogador,gols)