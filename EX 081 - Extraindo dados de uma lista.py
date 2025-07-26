lista = []
continuar = 'S'


while continuar == 'S':
        valor = int(input('Digite um número: '))
        lista.append(valor)
        continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]

        while continuar not in 'SsNn':
            continuar = str(input('Resposta Incorreta, Continuar? [S/N]')).strip().upper()[0]

print(f'foram digitados {len(lista)} números')
lista.sort(reverse=True)
print(f'A lista de valores ordenada de forma inversa é: {lista}')

if 5 in lista:
    print(f'O valor 5 foi encontrado na lista na posição {lista.index(5)}')
else:
    print('O valor 5 não foi encontrado na lista')


