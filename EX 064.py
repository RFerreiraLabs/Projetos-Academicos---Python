n = int(input('Digite um numero inteiro: '))
soma = 0
cont = 0

while n != 999:
    soma += n
    n = int(input('Digite outro numero inteiro: '))
    cont += 1

if n == 999:
    print('foram digitados {} numeros'.format(cont))
    print('a Soma dos {} numeros digitados é {}'.format(cont, soma))
