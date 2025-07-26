def notas(*num, sit= False):
    """ O função tem as seguintes informações:
    : parametro n: uma ou mais ntoas dos alunos (aceita várias)
    : param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com varias informações sobre a situação da turma.
    """
    dados = {'total': 0,
    'maior': 0,
    'menor': 0,
    'media': 0,
    'situaçao': 0}
    numeros = []
    numeros.append(num)
    dados['total'] = len(numeros[0])
    dados['maior'] = max(numeros[0])
    dados['menor'] = min(numeros[0])


    valor = 0
    for numero in numeros[0]:
        valor += numero
        media = valor / len(numeros[0])
    dados['media'] = float(f'{media:.2f}')

    if sit:
        if media >= 7:
            dados['situaçao'] = 'SITUAÇÃO ÓTIMA'

        elif media >= 5:
            dados['situaçao'] = 'SITUAÇÃO RAZOÁVEL'

        else:
            dados['situaçao'] = 'SITUAÇÃO RUIM'

    return(dados)



resultado = notas(2.5,5.5,4.5,6.9,2.0, 10.0, sit = True)
print(resultado)

