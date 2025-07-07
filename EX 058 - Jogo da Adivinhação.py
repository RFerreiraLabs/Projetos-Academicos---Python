from random import randint

computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um numero de 0 a 10.')
print('Será que voce consegue adivinhar? ')
acertou = False
palpite = 0

while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        else:
            print('Menos... tente mais uma vez')
print('Acertou com {} tentativas. PARABENS!! '.format(palpite))



'''numero = input('Digite um numero, BOA SORTE: ')

while not numero.isdigit():
    numero = input('Digite um número VÁLIDO: ')

numero = int(numero)

cont = 0

while numero != numeros_sorteados[0]:
    cont += 1
    numero = int(input('Que pena, voce errou! Tente novamente: '))

print ('PARABÉNS! VOCE ACERTOU!!')
print ('Voce precisou de {} tentativas'.format(cont)) '''
