pessoa = dict()
galera = []
continuar = 'S'
total = 0
mulheres = []

while continuar == 'S':
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if sexo in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')

    pessoa['Sexo'] = sexo
    idade = int(input('Idade: '))
    pessoa['Idade'] = idade
    galera.append(pessoa.copy())
    total += idade

    while True:
        continuar = str(input('Quer conitnuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! RESPONSA SOMENTE S OU N.')



print('-=' * 30)
print(galera)
print(f'O Grupo tem {len(galera)} pessoas')

media = total / len(galera)

print(f'A média de idades é de {media:.2f} anos')
print(f'As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['Sexo'] in 'Ff':
        print(f' {p['Nome']}', end='')
print()
print('lista das pessoas que estão acima da média: ')
for p in galera:
    if p['Idade'] >= media:
        print('   ',end='')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()
print('ENCERRADO')



