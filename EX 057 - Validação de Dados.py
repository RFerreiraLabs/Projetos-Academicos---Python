sexo = str(input('Digite seu sexo: [M/F]: ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Valor Inválido, Digite Novamente:')).strip().upper()[0]

print('Sexo {} digitado com sucesso'.format(sexo))

