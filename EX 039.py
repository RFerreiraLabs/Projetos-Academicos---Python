from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print ('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))

if idade == 18:
    print('Voce tem que se alistar imediatamente')

elif idade < 18:
    saldo = 18 - idade
    print('voce ainda nao tem 18 anos, ainda faltam {} anos pro alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))

elif idade > 18:
    saldo = idade - 18
    print('Voce já deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('seu alistamento foi em {}'.format(ano))


'''from datetime import date

ano_nascimento = int(input('Digite o ano que voce nasceu: '))
data_atual = date.today().year

idade = data_atual - ano_nascimento #trecho pra saber a minha idade fazendo a data atual - o ano em que nasci
ano_alistamento = ano_nascimento + 18 #trecho pra saber o ano em que devo me alistar

if idade < 18:
    anos_faltantes = 18 - idade # variavel que define quantos anos faltam para o alistamento
    meses_faltantes = anos_faltantes * 12
    print('Faltam {} meses pra voce se alistar'.format(meses_faltantes))

elif idade > 18:
    anos_atrasados = idade - 18
    meses_atrasados = anos_atrasados * 12
    print('voce ultrapassou {} meses do prazo de alistamento'.format(meses_atrasados))

else:
    print('é hora de voce se alistar')'''


