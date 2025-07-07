sexo = ''

while sexo not in ['F', 'M']:  # se atente a utilização de not in junto a estrutura while
    sexo = str(input('Digite seu sexo [M/F]: ')).upper()
    if sexo not in ['F', 'M']:
        print('Valor inválido, DIGITE NOVAMENTE')
print('FIM')
