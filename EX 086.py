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



for linhas in lista:
    print(linhas)