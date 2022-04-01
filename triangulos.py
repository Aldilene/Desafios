print('--=--' * 20)
print('Analisando triângulos')
print('--=--' * 20)
reta1 = float(input('primeiro tamanho '))
reta2 = float(input('segundo tamanho '))
reta3 = float(input('terceiro tamanho '))

if reta1 < reta2 + reta3 and reta2 < reta1+ reta3 and reta3 < reta1 + reta2:
    print('os tamanhos a cima podem formar uma triângulo')

else:
    print('os tamanhos á cima não podem formar um triângulo.')

