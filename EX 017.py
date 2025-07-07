from math import hypot
cat1 = float(input('digite o comprimento do cateto oposto: '))
cat2 = float(input('digite o comprimento do cateto adjacente: '))

hipot = hypot(cat1,cat2)
print('A hipotenusa é {:.2f}'.format(hipot) )
