r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta '))

if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3> r1):
    print('as retas a,b e c podem formar um triangulo')

else:
    print('as retas a,b e c não formam um triangulo')


