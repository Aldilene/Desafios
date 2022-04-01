salário = int(input('qual é o seu salário atual? '))
if salário <= 1500:
    novoSalário = salário + (salário * 15 / 100)

else:
    novoSalário = salário + (salário * 10 / 100)
print('quem ganhava {}, passou a ganhar {}'. format(salário, novoSalário))
