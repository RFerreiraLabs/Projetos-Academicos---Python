import random

numeros_sorteados = [random.randint(1,5)]

numero = input('Digite um número, BOA SORTE: ')

while not numero.isdigit():
    numero = input('Digite um número válido: ')

numero = int(numero)

while numero != numeros_sorteados[0]:
    numero = int(input('Alternativa incorreta, tente novamente: '))

print('Parabens! voce acertou')
