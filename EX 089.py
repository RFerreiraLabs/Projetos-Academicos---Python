continuar = 'S'
lista = []

notas = 0

while continuar == 'S':
    listai = []
    nome = str(input('Nome: '))
    listai.append(nome)
    nota1 = float(input('Nota 1: '))
    listai.append(nota1)
    nota2 = float(input('Nota 2: '))
    listai.append(nota2)

    media = (nota1 + nota2) / 2
    listai.append(media)
    lista.append(listai)

    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

print('-=' * 30)
print('No.    Nome      MEDIA')

for c, aluno in enumerate(lista):
    print(f'{c:<6} {aluno[0]:<10} {aluno[3]}')

while True:
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe)'))

    if mostrar == 999:
        print('Finalizado')
        break

    else:

        aluno_selecionado = lista[mostrar]
        print(f'Notas de {aluno_selecionado[0]} : {aluno_selecionado[1]} e {aluno_selecionado[2]}')
        print('-' * 30)



