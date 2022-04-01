from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-'*20)
print('adivinhe  qual número estou pensado entre 0 a 5.')
print('-=-'*20)
jogador = int(input('Qual número eu pensei?'))
print('PROCESSANDO....')
sleep(2)
if jogador == computador:
    print('você me venceu, PARABÉNS!')
else:
    print('Ganhei, pensei no número {}'.format(computador))
