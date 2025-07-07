cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
continuar = 'S'

while True:
    if continuar == 'S':

        while True:
            num = int(input('Digite um numero entre 0 e 20:'))
            if 0 < num < 20:
                break
            print('Tente novamente ', end='')
        print(f'Voce digitou o numero {cont[num]}')
        continuar = str(input('Voce quer continuar? [S/N]: ')).strip()[0].upper()

    else:
        break




