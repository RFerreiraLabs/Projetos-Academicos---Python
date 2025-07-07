numero = input('Digite um número: ')

while not numero.isdigit():
    numero = input('Digite um número válido: ')

numero = int(numero)

if numero % 2 == 0:
    print('o número {} é par!'.format(numero))

else:
    print('{} é impar'.format(numero))
