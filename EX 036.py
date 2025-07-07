valor = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu salário: '))
ano = int(input('Em quantos anos voce pretende pagar? '))

prestacao = valor / (ano * 12)

if prestacao <= salario * 0.3:
    print('PARABÉNS! seu emprestimo foi aprovado')
    print('O valor da prestação sera de R$ {:.2f}'.format(prestacao))


else:
    print('Infelizmente seu emprestimo foi negado')
    print('O valor da prestação de R$ {:.2f} excede 30% o valor seu salário'.format(prestacao))


    ''' OUTRA FORMA
    casa = float(input('Valor da casa: R$ '))
    salario = float(input('salario do comprador: R$: '))
    anos = int(input('Quantos anos de financiamento? ' ))
    prestação = casa / (anos * 12)
    minimo = salario * 30/100
    print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
    print('a prestação será de R${:.2f}'.format(prestacao))
    
    '''