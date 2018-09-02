# 6. Faça um Programa que leia um número e exiba o dia
# correspondente da semana. (1-Domingo, 2- Segunda, etc.), se
# digitar outro valor deve aparecer valor inválido.

dia_semana = int(input('Digite um número: '))
if (dia_semana == 1):
    print('Esse número correspondente ao Domingo')
elif (dia_semana == 2):
    print('Esse número correspondente a Segunda-feira')
elif (dia_semana == 3):
    print('Esse número correspondente a Terça-feira')
elif (dia_semana == 4):
    print('Esse número correspondente a Quarta-feira')
elif (dia_semana == 5):
    print('Esse número correspondente a Quinta-feira')
elif (dia_semana == 6):
    print('Esse número correspondente a Sexta-feira')
elif (dia_semana == 7):
    print('Esse número correspondente a Sábado')
else:
    print('Dia inválido.')

