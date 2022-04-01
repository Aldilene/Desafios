from random import choice
usuario= int(input('Qual valor o computador vai escolher? '))
num1 = int(65)
num2 = int(62)
num3 = int(29)
num4 = int(15)
num5 = int(42)
lista= [num1, num2, num3, num4, num5]
escolhido = choice(lista)
print('o número escolhido foi {}'.format(escolhido))
if usuario == escolhido:
    print('você venceu')
else:
    print('você perdeu')
