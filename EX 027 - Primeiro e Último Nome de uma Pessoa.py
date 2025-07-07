nome = str(input('Digite seu nome completo: ')).strip().upper()
nome_div = nome.split()
print('Seu primeiro nome é {}'.format(nome_div[0]))
print('Seu ultimo nome é {}'.format(nome_div[-1]))
