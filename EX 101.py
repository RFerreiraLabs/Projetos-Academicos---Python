from datetime import date



def voto(idade):
    if idade > 18 and idade < 65:
        print(f' Com {idade} anos: VOTO OBRIGATÓRIO')

    elif idade < 18:
        print(f' Com {idade} anos: NÃO VOTA')

    else:
        print(f' Com {idade} anos: VOTO OPCIONAL')



# PROGRAMA PRINCIPAL
nasc = int(input('Em que ano voce nasceu? '))
atual = date.today().year
idade = atual - nasc

voto(idade)
