a = float(input('Digite a primeira nota: '))
b = float(input('Digite a segunda nota: '))

media = (a + b) / 2

print('tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(a, b, media))

if media < 5:
    print('REPROVADO')

elif media > 5 and media < 6.9:
    print('RECUPERAÇÃO')

else:
    print('APROVADO')