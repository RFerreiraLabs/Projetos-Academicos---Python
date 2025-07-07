frase = str(input('Digite uma frase: ')).strip().upper()

print('a letra a aparece {} vezes'.format(frase.count('A')))
print('A primeira letra a aparece na posicao {}'.format(frase.find('A')+1))
print('A ultima vez que aparece é na posicao {}'.format(frase.rfind('A')+1))

