from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('o atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade > 9 and idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print ('Classificação: SENIOR')
else:
    print ('Classificação: MASTER')

'''from datetime import date

nascimento = int(input('Digite o ano do seu nascimento: '))
data_atual = date.today().year
idade = data_atual - nascimento

if idade < 9:
    print('MIRIM')

elif idade > 9 and  idade < 14:
    print ('INFANTIL')

elif idade > 14 and idade < 19:
    print ('JUNIOR')

elif idade > 19 and idade <20:
    print ('SENIOR')

elif idade > 20:
    print ('MASTER')'''