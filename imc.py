peso = float(input('digite seu peso (kg): '))
altura = float(input('digite a altura (m) :'))
imc = peso / (altura ** 2)
print('o IMC dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('você está abaixo do peso normal')
elif imc <= 25:
    print('vocÊ está no peso ideal')
elif imc <= 30:
    print('você está com sobrepeso')
elif imc <= 40:
    print('você está com obesidade')

else:
    print(' vocÊ está com obesidade mórbida')