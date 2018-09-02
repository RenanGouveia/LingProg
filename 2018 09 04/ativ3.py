# 3. Faça um programa para a leitura de duas notas parciais de um aluno.
    #   O programa deve calcular a média alcançada por aluno e apresentar:
    # - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    # - A mensagem "Reprovado", se a média for menor do que sete;
    # - A mensagem "Aprovado com Distinção", se a média for igual a dez.

import statistics

nota1 = int(input('Digite a nota 1: '))
nota2 = int(input('Digite a nota 2: '))

media = (nota1 + nota2) / 2
aprovado = 7.0

if (media == 10):
    print("Aprovado com Distinção")
elif (media >= aprovado):
    print("Aprovado")
else:
    print("Reprovado")

