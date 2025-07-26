from datetime import date

atual = date.today().year

cadastro = dict()

cadastro['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
cadastro['Idade'] = atual - nascimento
cadastro['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))

if cadastro['CTPS'] == 0:

    for k, v in cadastro.items():
        print(f'{k} tem o valor {v}')

else:

    cadastro['Contratação'] = int(input('Ano de Contratação: '))
    cadastro['Salário'] = float(input('Salário: '))
    idade = atual - nascimento
    aposentar = cadastro['Contratação'] + 35
    anoaposentar = aposentar - nascimento
    cadastro['Aposentadoria'] = anoaposentar

    for k, v in cadastro.items():
        print(f'{k} tem o valor {v}')





