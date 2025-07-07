print ('{:=^40}'.format('LOJAS RODY'))
preco = float(input('Digite o preço do produto: '))
print('''formas de pagamento!
 [1] à vista dinheiro/cheque
 [2] à vista cartão
 [3] 2x no cartão
 [4] 3x ou mais no cartão''')
pgto = int(input('Qual a forma de pagamento? '))


if pgto == 1:
    preco = preco - (preco / 100) * 10
    print('Seu produto teve um desconto de 10% e o preço é R$ {:.2F} reais'.format(preco))

elif pgto == 2:
    preco = preco - (preco / 100) * 5
    print('Seu produto teve um desconto de 5% e o preço é R$ {:.2f} reais'.format(preco))

elif pgto == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f}'.format(parcela))
    print ('Seu produto não tem desconto e o preço é R$ {:.2f} reais'.format(preco))

elif pgto == 4:
    total = preco + (preco * 0.20)
    totalparc = int(input('quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS'.format(totalparc, parcela))
    print('Seu produto teve um juros de 20% e o preço é R$ {:.2f} reais'.format(total))
else:
    total = 0
    print('Opção inválida de pagamento. Tente novamente!')
    print ('Sua compra é R$ {:.2f} reais'.format(total))

