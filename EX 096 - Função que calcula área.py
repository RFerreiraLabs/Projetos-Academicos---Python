def area ():
    print('CONTROLE DE TERRENOS')
    print('-' * 20)
    largura = float(input('LARGURA (m): '))
    comprimento = float(input('COMPRIMENTO (m): '))
    area = largura * comprimento
    print(f'A área de um terreno {largura} x {comprimento} é de {area} m².')

area()
