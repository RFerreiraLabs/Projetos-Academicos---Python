jogador = dict()
partidas = list()
time = list()


while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))
    partidas.clear()
    for c in range (0,tot):
        partidas.append(int(input(f'  Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if resp in "SN":
            break
        print('ERRO! Responda apenas S ou N! ')
    if resp == 'N':
        break

print('COD ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para Parar!) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Nao existe jogador com código {busca}! ')

    else:
        print(f' -- LEVANTAMENTO DO  JOGADOR {time[busca]['Nome']}: ')
        for i, gols in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {gols} gols!')
    print('-' * 40)
