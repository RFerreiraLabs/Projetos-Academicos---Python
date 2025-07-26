aluno = {'Nome':'' , 'Média':''}
print(aluno)

aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno['Nome']}: '))

print(f'Nome é igual a {aluno['Nome']} ')
print(f'Média é igual a {aluno['Média']} ')

if aluno['Média'] >= 5:
    print('Situação é igual a APROVADO')
else:
    print('Situação é igual a REPROVADO!')


