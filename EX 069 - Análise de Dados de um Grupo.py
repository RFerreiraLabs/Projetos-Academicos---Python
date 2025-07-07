
continuar = 'S'
totalmaior = 0
homem = 0
mulher = 0


while True:

    if continuar == 'S':

        idade = int(input( 'Digite a idade: '))
        sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
        while sexo not in "MF":
            sexo = str(input('Digite o sexo: [M/F]')).upper().strip()[0]

        if idade > 18:
            totalmaior += 1

        if sexo == 'M':
            homem += 1

        if sexo == 'F' and idade < 20:
            mulher += 1

        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        while continuar not in "SN":
            continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    elif continuar == 'N':
        print(f'Total de pessoas com mais de 18 anos: {totalmaior}')
        print(f'Ao todo temos {homem} homens cadastrados')
        print(f'E temos {mulher} mulheres com menos de 20 anos.')
        break
