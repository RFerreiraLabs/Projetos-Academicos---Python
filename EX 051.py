primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10-1) * razao

for c in range (primeiro, decimo + razao, razao):
    print ('{}'.format(c), end= ' => ')
print('ACABOU')


'''termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da Progressao Aritmetica: '))

for x in range (1,10+1):
    termonovo = termo + (x - 1) * razao
    print(termonovo)'''