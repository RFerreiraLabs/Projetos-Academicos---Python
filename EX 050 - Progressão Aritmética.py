s = 0
cont = 0

for n in range (1,7):
    x = int(input('Digite o {} valor: '.format(n)))
    if x % 2 == 0:
        s = x + s
        cont = cont + 1
print('voce informou {} numros e a soma dos numeros inteiros é {}'.format(cont,s))
