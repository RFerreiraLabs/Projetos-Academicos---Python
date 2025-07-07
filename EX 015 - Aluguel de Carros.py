km = int(input('Digite a quantidade de KM rodados: '))
dias = int(input('Digite a quantidade de dias alugados: '))

precokm = km * 0.15
precodias = dias * 60
totalgasto = precokm + precodias

print('O total gasto é de {:.2f} R$'.format(totalgasto))
