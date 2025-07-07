salario = float(input('Qual o seu salário? '))

if salario > 1250.00:
    aumento = salario * 1.10
    valor_aumento = aumento - salario
    print('voce teve um aumento de {:.2f} reais'.format(valor_aumento))
    print('Seu salario agora é de {:.2f} reais'.format(aumento))

else:
    if salario <= 1250.00:
        aumento = salario * 1.15
        valor_aumento = aumento - salario
        print('Voce teve um aumento de {:.2f} reais'.format(valor_aumento))
        print('Seu salario agora é de {:.2f} reais'.format(aumento))

