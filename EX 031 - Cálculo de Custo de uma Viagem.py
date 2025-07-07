distancia = float(input('Digite a Distância: '))
print('Voce esta prestes a começar uma viagem de {} Km.'.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f} reais'.format(preco))



'''if distancia <= 200:
    preco = distancia * 0.50
    print('O preço da passagem é R$ {:.2f} reais'.format(preco))

else:
    preco = distancia * 0.45
    print('O preço da passagem é R$ {:.2f} reais'.format(preco))'''

