lista = []

for cont in range(0,5):
    lista.append(int(input('Digite um valor: ')))

lista.sort()
print(lista)

for c,v in enumerate(lista):
    print(f' O valor {v} foi encontrado na posição {c}')

print(f' O menor valor digitado foi {lista[0]}')
print(f' O maior valor digitado foi {lista[4]}')