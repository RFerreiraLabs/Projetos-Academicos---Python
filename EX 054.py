'''from datetime import date

atual = date.today().year
cont = 0
acumulo = 0

for idade in range (1,7+1):
    ano = int(input('Qual seu ano de nascimento? '))

    if atual - ano < 18:
        cont += 1

    elif atual - ano >= 18:
        acumulo += 1

print('{} pessoas não atingiram a maioridade e {} pessoas já atingiram'.format(cont, acumulo))'''


from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range (1,8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('Ao todo tivemos {} pessoas menores de idade'.format(totmenor))
