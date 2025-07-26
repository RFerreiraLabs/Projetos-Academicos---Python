'''expressao = input('Digite uma expressão: ')

abertos = expressao.count('(')
fechados = expressao.count(')')


if abertos == fechados:
    print('A expressão está correta')
else:
    print('A expressão está incorreta')'''

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')

    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()

        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está válida!')

else:
    print('Sua expressão não é válida')