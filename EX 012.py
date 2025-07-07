produto = float(input('Digite o valor do produto: '))

desconto = produto * 0.05

final = produto - desconto

print('o valor do produto com desconto de 5% é {:.2F} reais'.format(final))