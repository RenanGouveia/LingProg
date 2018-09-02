# 7. Faça um programa que lê as duas notas parciais obtidas por um
# aluno numa disciplina ao longo de um semestre, e calcule a sua
# média. A atribuição de conceitos obedece à tabela abaixo:
# Média de Aproveitamento Conceito
# Entre 9.0 e 10.0 = A
# Entre 7.5 e 9.0  = B
# Entre 6.0 e 7.5  = C
# Entre 4.0 e 6.0  = D
# Entre 4.0 e zero = E
# O algoritmo deve mostrar na tela as notas, a média, o conceito
# correspondente e a mensagem “APROVADO” se o conceito for A, B
# ou C ou “REPROVADO” se o conceito for D ou E.

import statistics

notas = []
aluno = str(input('Nome do aluno: '))
for i in range(2):
    nota = float(input('Digite a nota do aluno: %s ' %aluno))
    notas.insert(i, nota)

media = sum(notas)/2

if (media >= 9.0):
    print('O %s ' % aluno, 'ficou com média: %s ' % media, 'com notas: %s ' % notas[:len(notas)] ,'e foi Aprovado - A')
elif (media >= 7.5 and media < 9.0):
    print('O %s ' % aluno , 'ficou com média: %s ' % media, 'com notas: %s ' % notas[:len(notas)] ,'e foi Aprovado - B')
elif (media >= 6.0 and media <= 7.5):
    print('O %s ' % aluno,  'ficou com média: %s ' % media , 'com notas: %s ' % notas[:len(notas)] ,'e foi Aprovado - C')
elif (media >= 4.0 and media <= 6.0):
    print('O %s ' % aluno, 'ficou com média: %s ' % media, 'com notas: %s ' % notas[:len(notas)],'e foi Reprovado - D')
elif (media < 4.0 and media > 0):
    print('O %s ' % aluno, 'ficou com média: %s ' % media, 'com notas: %s ' % notas[:len(notas)], 'e foi Reprovado - E')
else:
    print('A um problema com as notas, peça que revejam.')

