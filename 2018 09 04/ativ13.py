#13. Faça um programa que peça uma nota, entre zero e dez. Mostre
#uma mensagem caso o valor seja inválido e continue pedindo até
#que o usuário informe um valor válido.

i = 0
while(i == 0):
    x = int(input('Digite uma nota de 0 a 10: '))
    if(x < 0 or x > 10):
        print('Valor inválido: %s ' %x)
        x = 0
    else:
        print('Nota válida: %s' %x)
        break