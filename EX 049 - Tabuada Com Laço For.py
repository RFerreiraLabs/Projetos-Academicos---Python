n = int(input('Digite um numero: '))

for x in range (1,10+1):
    s = x * n
    print('{} x {} = {}'.format(x,n,s)) # pode ser substituido por (num, c, num * c)
