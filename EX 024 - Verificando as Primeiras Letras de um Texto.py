# CRIE UM PROGRAMA QUE LEIA O NONME DE UMA CIADDE E DIGA SE ELA COMEÇA OU NÃO COM O NOME 'SANTO'


cidade = str(input('Digite o nome de uma cidade: ')).strip()

contador = cidade.upper().count('Santo',0, 5)


while True:

    if contador > 0:
        print('A cidade {} começa com santo'.format(cidade))
        break

    else:
        print('A cidade {} nao começa com santo'.format(cidade))
        break

# outra resoluçao
# cidade = str(input("em que cidade voce nasceu? ')).strip()
print(cidade[:5].upper()== 'SANTO')
