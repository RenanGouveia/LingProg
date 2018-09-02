#16. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

number = 1
while(number <= 50):
    if(number%2 != 0):
        print('Ímpar: %s ' %number)
    number = number + 1


