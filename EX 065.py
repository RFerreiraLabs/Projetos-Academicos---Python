resp = 'S'
media = soma = quant = maior = menor = 0

while resp in "Ss":
    num = int(input('Digite um número: '))
    quant += 1
    soma += num
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Voce quer continuar? [S/N]')).upper().strip()[0]

media = soma / quant
print('Voce digitou {} numeros e a média foi {}'.format(quant, media))
print('O maior numero digitado foi {} e o menor foi {}'.format(maior, menor))






