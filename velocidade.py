vel= float(input('Qual a velocidade do carro? '))
multa = (vel - 80) *7
if vel > 80:
    print('você excedeu o limite de 80km/h e está sendo multado')
    print('o valor da multa é de: R${:.2f}'.format(multa))
