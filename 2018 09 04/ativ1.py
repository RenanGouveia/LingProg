#1. Faça um Programa que peça dois números e imprima o maior deles.
#
number1 = input('Digite um número: ')
number2 = input('Digite outro número: ')

if number1 > number2:
	print('O maior é o: %s' %number1 )
elif number2 > number1:
	print('O maior é o: %s' %number2)
else:
	print(' são iguais. ')

