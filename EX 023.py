# FAÇA UM PROGRAMA QUE LEIA UM NUMERO DE 0 A 9999 E MOSTRE NA TELA CADA UM DOS SEUS DIGITOS SEPARADOS

numero = int(input('Digite um numero: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10


print('Analisando o numero {}'.format(numero))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar {}'.format(m))


