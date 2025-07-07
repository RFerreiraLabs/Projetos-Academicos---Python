r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))


if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    print('os segmentos acima podem formar um triangulo')

    if r1 == r2 and r2 == r3:
        print('é um triangulo equilatero')

    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('é um triangulo escaleno')

    else:
        print('É isosceles')

else:
    print('os segmentos não formam um triangulo')


