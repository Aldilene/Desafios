from datetime import date
ano = int(input('Que ano você quer analisar? digite 0 para o ano atual: '))
if ano == 0:
    ano= date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('o ano {} é BISSEXTO '.format(ano))
else:
    print('o ano {} não é BISSEXTO '.format(ano))
