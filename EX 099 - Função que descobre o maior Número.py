

def maior():
    numeros = []
    resp = 'S'

    while resp == 'S':
        numero = int(input('Digite um valor: '))
        numeros.append(numero)

        if numero == 0:
            print('Foram informados 0 valores ao todo')
            print('O maior valor informado foi 0')
            numeros.clear()


        while True:
            resp = str(input('Quer Adicionar outro número? [S/N]')).upper().strip()[0]
            if resp in 'SN':
                break

    print('Analisando os valores passados...')
    print(f'{numeros} Foram informados {len(numeros)} valores ao todo.')
    print(f'O maior valor infomado foi {max(numeros)} ')

maior()
