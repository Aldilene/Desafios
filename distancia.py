distância= float(input('qual a distância da viagem?'))
print('você fará uma viagem de {}km'.format(distância))
if distância <= 200:
    preco= 0.50 * distância
    print('sua viagem irá custar {}'.format(preco))
else:
    preco = 0.45 * distância
print('sua viagem irá custar R${:.2f}'.format(preco))
