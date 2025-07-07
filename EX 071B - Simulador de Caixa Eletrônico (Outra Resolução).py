print('=' * 30)
print(' ' * 10, 'BANCO CEV')
print('=' * 30)

valor = int(input('Qual valor voce quer sacar? '))
total = valor
cedula = 50
totalced = 0

while True:

    if total >= cedula:
        total -= cedula
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cedulas de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalced = 0
        if total == 0:
            break
