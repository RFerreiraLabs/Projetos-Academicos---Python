palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso',
            'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
            'programador', 'futuro')

for palavra in palavras:
    contadora = palavra.count('a')
    contadore = palavra.count('e')
    contadori = palavra.count('i')
    contadoro = palavra.count('o')
    contadoru = palavra.count('u')


    if contadora >= 1:
        contadora = 'a ' * contadora
    elif contadora <= 1:
        contadora = ''

    if contadore >= 1:
        contadore = 'e ' * contadore
    elif contadore <= 1:
        contadore = ''

    if contadori >= 1:
        contadori = 'i ' * contadori
    elif contadori <= 1:
        contadori = ''


    if contadoro >= 1:
        contadoro = 'o ' * contadoro
    elif contadoro <= 1:
        contadoro = ''


    if contadoru >= 1:
        contadoru = 'u ' * contadoru
    elif contadoru <= 1:
        contadoru = ''


    print(f'Na Palavra {palavra} temos {contadora}{contadore}{contadori}{contadoro}{contadoru}')
