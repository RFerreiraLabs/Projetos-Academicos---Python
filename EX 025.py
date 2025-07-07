nome = str(input('Digite um nome: ')).strip()

if nome.lower()[1:].count('silva') > 0:
    print('possui Silva no nome')

else:
    print('não possui Silva no nome')



#outra resolução
# nome = str(input('Digite um nome: ')).strip()
# print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))