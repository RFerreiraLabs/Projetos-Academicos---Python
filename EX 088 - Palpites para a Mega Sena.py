import random
from time import sleep

listas = []

print('-' * 40)
print(' ' * 10, 'JOGO DA MEGASENA', ' ' * 10)
print('-' * 40)
jogos = int(input('Quantos jogos voce quer que eu sorteie? '))

for n in range(jogos):
    lista = []
    while len(lista) < 6:
        numero = random.randint(1,60)
        if numero not in lista:
            lista.append(numero)
    listas.append(lista)

for i, jogos in enumerate(listas, 1):
    sleep(1)
    print(f'jogo N {i}: {jogos}')







