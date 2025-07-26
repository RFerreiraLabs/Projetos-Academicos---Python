jogadores = []
jogador = dict()
continuar = 'S'

while continuar == 'S':
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))
    jogador['gols'] = []
    jogador['total'] = 0

    for partida in range(partidas):
        gol = int(input(f'quantos gols na partida {partida+1}? '))
        jogador['gols'].append(gol)
        jogador['total'] += gol

    jogadores.append(jogador.copy())

    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if continuar in "SN":
            print('-' * 30)
            break
        print('ERRO! RESPONDA SOMENTE S OU N')

print('-=' * 40)
print('cod     nome        gols         total')
for i, jogador in enumerate(jogadores):
    print(f'{i}      {jogador['Nome']}          {jogador['gols']}            {jogador['total']}')

while True:
    cod = int(input('Mostrar dados de qual jogador? '))

    if cod == 999:
        break
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[cod]['Nome']}: ')
        for i,gols in enumerate(jogadores[cod]['gols']):
            print(f'    No jogo {i+1} fez {gols} gols')





