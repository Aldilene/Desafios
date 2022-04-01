from datetime import date
atual = date.today().year
nasc = int(input('que ano você nasceu? '))
idade= atual - nasc

if idade == 18:
    print('você tem {} anos, e está na hora de se alistar'.format(idade))

elif idade < 18:
    faltam = 18 - idade
    print('você tem {} anos, faltam {} anos para se  alistar nos serviço militar'.format(idade, faltam))
    ano = atual + faltam
    print('seu alistamente será no ano {}'.format(ano))

elif idade > 18:
    passou = idade - 18
    print('você tem {} anos e já passou {} anos da idade de se alistar'.format(idade, passou))
    ano = atual - passou
    print('você deveria ter se alistado em {}'.format(ano))
