lista = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

somapar = 0
terceira = 0
soma_coluna = 0


for linha in range (0,3):
    for coluna in range (0,3):
        valor = int(input(f'Digite um valor para: [{linha}],[{coluna}]  '))
        lista[linha][coluna] = valor

        if valor % 2 == 0:
            somapar += valor

for linha in lista:
    soma_coluna += linha[2]


for linhas in lista:
    print(linhas)


mai = max(lista[1])

print(somapar)
print(soma_coluna)
print(mai)
