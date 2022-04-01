from datetime import date
atual = date.today().year
ano = int(input('em que ano você nasceu? '))
idade = atual - ano
print('o atleta tem {} anos, '.format(idade))
if idade <= 9:
    print('sua categoria é MIRIM')
elif idade > 9 and idade <=14:
    print('sua categoria é INFANTIL')
elif idade > 14 and idade <=19:
    print('sua categoria é JÚNIOR')
elif idade >19 and idade <=25:
    print('sua categoria é SÊNIOR')
elif idade >25:
    print('sua categoria é MASTER')
