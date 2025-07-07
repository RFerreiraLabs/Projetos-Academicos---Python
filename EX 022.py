#CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
# O NOME COM TODAS AS LETRAS MAIUSCULAS
# O NOME COM TODAS AS LETRAS MINUSCULAS
# QUANTAS LETRAS AO TOTAL SEM CONSIDERAR ESPAÇOS
# QUANTAS LETRAS TEM O PRIMEIRO NOME


nome = str(input('digite o nome: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maíusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))


# outra forma de encontrar o primeiro nome

primeiro = nome.split()

print('Seu primeiro nome é {} e ele tem {} letras'.format(primeiro[0], len(primeiro[0])))



