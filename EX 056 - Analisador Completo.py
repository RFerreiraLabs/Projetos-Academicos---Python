somaidade = 0
mediaidade = 0
nomevelho = ''
maioridadehomem = 0
totmulher20 = 0

for p in range (1,5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1


mediaidade = somaidade / 4
print('a media de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho se chama {} e tem {} anos'.format(nomevelho, maioridadehomem))
print('Ao todo sao {} mulheres com menos de 20 anos'.format(totmulher20))
