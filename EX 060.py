numero = int(input('Digite um número: '))
fatorial = 1
cont = numero


while numero > 1:
    fatorial = fatorial * numero
    print(fatorial, end= '->')
    numero = numero - 1

print('O fatorial de {} é {}'.format(cont,fatorial))

n = int(input('Digite um numero para calcular o fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end= '')

while c > 0:
    print('{}'.format(c), end= '')
    print(' x ' if c > 1 else ' = ', end= '')
    f *= c
    c -= 1
print('{}'.format(f), end='')