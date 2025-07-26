jogador = dict()
jogador['Nome'] = str(input('Nome do jogador: '))
partidas = int(input('Quantas Partidas foram jogadas: '))
jogador['gols'] = []
jogador['total'] = 0

for partida in range(partidas):
    gol = int(input(f'Quantos gols na partida {partida+1}? '))
    jogador['gols'].append(gol)
    jogador['total'] += gol

print('-=' * 30)
print(jogador)
print('-=' * 30)

for i, gol in enumerate(jogador['gols']):
    print(f'Na partida {i+1}, fez {gol} gols.')

print(f'Foi um total de {jogador['total']} gols.')