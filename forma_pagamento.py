print('{:=^40}'.format('LOJAS ALDILENE'))
preço = float(input('Qual o valor?' ))

print(''' escolha a forma de pagamento:
[1] á vista no dinheiro
[2] á vista no cartão
[3] até 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('qual a opção? '))

if opção ==1:
    Avista = preço -(preço * 10 / 100)
    print('o pagamento a vista sai com 10% de desconto e você pagará {}'.format(Avista))

elif opção == 2:
    AvistaCartão = preço - (preço * 5 / 100)
    print('o pagamento a vista no cartão tem 5% de desconto e você pagará {}'.format(AvistaCartão))

elif opção == 3:
    total = preço
    parcela = total /2
    print('sua compra parcelada em 2x no cartão sua parcela será no valor de {}'.format(parcela))
    print('você irá pagar um total de {}'.format(preço))

elif opção == 4:
    total= preço + (preço * 20 / 100)
    totalparcelas = int(input('quantas vezes vocÊ quer parcelar? '))
    parcelas = total /totalparcelas
    print('sua compra será parcelada em {}x de R$ {:.2f} COM JUROS de 20%'.format(totalparcelas, parcelas))
    print('sua compra de {:.2f} vai custa {:.2f} no final'. format(preço,total))
else:
    total = 0
    print('opção inválida de pagamento, tente novamente')
