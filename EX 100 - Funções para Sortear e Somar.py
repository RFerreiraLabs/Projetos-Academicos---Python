from random import randint
from time import sleep


numeros = list()
somapares = 0

def sorteia(lista):
    print(f'Sorteando 5 valores da lista: ', end=' ')
    for c in range (0,5):
        numero = randint(1,10)
        lista.append(numero)
        print(f'{numero}',end=' ',flush=True)
        sleep(0.3)
    print('PRONTO!')


def somapar(lista):
    somapares = 0
    for numero in lista:
        if numero % 2 == 0:
            somapares += numero
    print(f'Somando os valores pares de {lista}, temos {somapares}')


sorteia(numeros)
somapar(numeros)
