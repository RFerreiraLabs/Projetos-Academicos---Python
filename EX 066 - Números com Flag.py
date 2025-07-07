soma = cont = 0

while True:
    num = int(input('Digite outro numero (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num

print(f'Foram digitados {cont} números e a soma foi {soma}')
