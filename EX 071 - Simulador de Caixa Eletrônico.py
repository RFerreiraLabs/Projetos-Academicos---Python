print('=' * 30)
print(' ' * 10, 'BANCO CEV')
print('=' * 30)

valor = int(input('Qual valor voce quer sacar? '))
total = valor
cedula50 = 50
cedula20 = 20
cedula10 = 10
cedula1 = 1
total_cedulas50 = total_cedulas20 = total_cedulas10 = total_cedulas1 = 0

while True:
    if total >= cedula50:
        total -= cedula50
        total_cedulas50 += 1


    elif total >= cedula20:
        total -= cedula20
        total_cedulas20 += 1


    elif total >= cedula10:
        total -= cedula10
        total_cedulas10 += 1


    elif total >= cedula1:
        total -= cedula1
        total_cedulas1 += 1


    if total == 0:
        print(f'total de {total_cedulas50} cédulas de R$ 50')
        print(f'total de {total_cedulas20} cédulas de R$ 20')
        print(f'total de {total_cedulas10} cédulas de R$ 10')
        print(f'total de {total_cedulas1} cédulas de R$ 1')
        break


