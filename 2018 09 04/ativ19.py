#19. Faça um programa que calcule o fatorial de um número inteiro
#fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

x = int(input('Digite um valor para ser calculado o fatorial: '))
i = x - 1
valor = x * i
while(True):
    i = i - 1
    if(i != 0):
        total = valor * i
        valor = total
    else:
        print(total)
        break