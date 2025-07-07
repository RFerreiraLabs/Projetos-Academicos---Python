import random

for c in range (1,6):
    num = random.randint(1,10)
    print(num, end=' ')
    ordenados = sorted(num)
    print(f'O menor numero encontrado é {num[0]}')
    print(f'O maior numero encontrado é {num[4]}')
