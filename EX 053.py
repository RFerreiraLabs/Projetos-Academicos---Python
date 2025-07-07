frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) -1, -1, -1): # AQUI O PROGRAMA SELECIONA O VALOR DE CADA POSIÇÃO DE LETRA (NO CASO DE TRAS PRA FRENTE)
    inverso += junto[letra]
print(junto, inverso)

if inverso == junto:
    print('temos um palíndromo')
else:
    print('a frase digitada não é um palindromo')

