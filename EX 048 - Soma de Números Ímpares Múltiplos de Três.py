s = 0
cont = 0

for mult in range (1,500+1, 2):
    if mult % 3 == 0:
        cont += 1
        s += mult

print('A soma de todos os {} valores solicitados é {}'.format(cont, s))
