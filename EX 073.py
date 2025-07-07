brasileirao = ('Flamengo', 'Cruzeiro', 'Bragantino', 'Palmeiras', 'Bahia', 'Fluminense', 'Ateltico - MG',
               'Botafogo', 'Mirassol', 'Corinthians', 'Gremio', 'Ceará', 'Vasco da Gama', 'São Paulo',
               'Santos','Vitória', 'Internacional', 'Fortaleza', 'Juventude', 'Sport')

print('-=' * 30)
print(f'Os primeiros colocados do Brasileirão são: {brasileirao[0:6]}')
print('-=' * 30)
print(f'Os quatro últimos colocados da tabela são: {brasileirao[-4:]}')
print('-=' * 30)
print(f'Os times em ordem alfabetica: {sorted(brasileirao)}')
print('-=' * 30)

pos = (brasileirao.index('Santos'))
print(f'O Santos está em {pos +1} lugar')

