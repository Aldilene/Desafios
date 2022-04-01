num = int(input('Digite um número: '))
print( '''escolha uma das opções abaixo para conversão:
[1] converter para binário.
[2] converter para octal
[3] converter para hexadecimal''')
opção = int(input('sua opção: '))
if opção == 1:
    print('{} convertido para binário é igual a {} '.format(num, bin(num)[:2]))
elif opção == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[:2]))
elif opção == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[:2]))

else:
    print('opção inválida, tente novamente. ')