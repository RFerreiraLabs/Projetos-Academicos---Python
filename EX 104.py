def leiaint(num):
   while not str(num).isnumeric():
        print('ERRO! Digite um número válido.')
        num = input('Digite um número: ')
   if num.isnumeric():
        print(f'Voce acabou de digitar um número inteiro válido {num}.')



num = input('Digite um número: ')
leiaint(num)

