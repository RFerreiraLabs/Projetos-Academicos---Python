velocidade = input('Digite a Velocidade: ')
multa = 0

while not velocidade.isdigit():
    velocidade = input('Digite um valor válido: ')

velocidade = int(velocidade)

if velocidade > 80:
    print('Voce foi MULTADO!')
    multa = (velocidade - 80) * 7.00
    print('Sua multa custará {:.2f}'.format(multa))

else:
    print('Siga e tenha uma boa viagem')
