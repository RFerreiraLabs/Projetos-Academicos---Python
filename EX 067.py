num = int(input('Digite um número: '))
c = 1

while True:

    if num < 0:
        print('fim do codigo')
        break


    for c in range (1,11):
        print (f' {num} x {c} = {c * num}')

    num = int(input('Deseja saber a tabuada de outro valor?: '))