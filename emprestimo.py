valor = float(input('qual o valor da casa R$? '))
salário = float(input('Quanto é o seu salário R$? '))
anos = int(input('em quantos anos você vai pagar? '))
prestação= valor / (anos * 12)
minimo = salário * 30/100
print('para pagar uma casa de R${:.2f} em {} anos'.format(valor,anos))
print('a prestação será de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print("empréstimo APROVADO!")
else:
    print('empréstimo NEGADO!')