nota = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
média = (nota + nota2) / 2

if média >= 7:
    print(' tendo as notas {} +  {} a média é: {}, APROVADO'.format(nota, nota2, média))

elif média > 5 and média < 7:
    print('tendo as notas {} + {} a média é: {}, o aluno está em RECUPERAÇÂO'.format(nota, nota2, média))

elif média <= 5:
    print('tendo as notas {} + {} a média é: {}, O aluno está REPROVADO'.format(nota, nota2, média))
