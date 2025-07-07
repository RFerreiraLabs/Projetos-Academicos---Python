from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 10)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 10)

if computador == 0: #pedra
    if jogador == 0:
        print('EMPATE')

    elif jogador == 1:
        print('JOGADOR VENCE')

    elif jogador == 2:
        print('COMPUTADOR VENCE')

    else:
        print('JOGADA INVÁLIDA')

elif computador == 1: # Papel
    if jogador == 0:
        print('COMPUTADOR VENCE')

    elif jogador == 1:
        print('EMPATE')

    elif jogador == 2:
        print('JOGADOR VENCE')

    else:
        print('JOGADA INVÁLIDA')


elif computador == 2: #tesoura
    if jogador == 0:
        print('JOGADOR PERDE')

    elif jogador == 1:
        print('COMPUTADOR VENCE')

    elif jogador == 2:
        print('EMPATE')

    else:
        print('JOGADA INVÁLIDA')



''' import random

jokenpo = ['pedra', 'papel', 'tesoura']
palavra_aleatoria = random.choice(jokenpo)

escolha = str(input('PEDRA, PAPEL OU TESOURA?: '))
print('JO KEEN PO!!')

if escolha == 'pedra' and palavra_aleatoria == 'tesoura':
    print (palavra_aleatoria)
    print ('PARABENS VOCE VENCEU!')

elif escolha == 'pedra' and palavra_aleatoria == 'papel':
    print(palavra_aleatoria)
    print ('QUE PENA, VOCE PERDEU! ')

elif escolha == 'pedra' and palavra_aleatoria == 'pedra':
    print(palavra_aleatoria)
    print ('EMPATE! ')


elif escolha == 'papel' and palavra_aleatoria == 'tesoura':
    print(palavra_aleatoria)
    print ('QUE PENA, VOCE PERDEU!')

elif escolha == 'papel' and palavra_aleatoria == 'papel':
    print(palavra_aleatoria)
    print ('EMPATE! ')

elif escolha == 'papel' and palavra_aleatoria == 'pedra':
    print(palavra_aleatoria)
    print ('PARABENS, VOCE VENCEU!! ')


elif escolha == 'tesoura' and palavra_aleatoria == 'papel':
    print(palavra_aleatoria)
    print ('PARABENS, VOCE VENCEU!! ')

elif escolha == 'tesoura' and palavra_aleatoria == 'pedra':
    print(palavra_aleatoria)
    print ('QUE PENA, VOCE PERDEU! ')

elif escolha == 'tesoura' and palavra_aleatoria == 'tesoura':
    print(palavra_aleatoria)
    print('EMPATE!') '''

