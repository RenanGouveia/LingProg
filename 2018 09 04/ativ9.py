# 9. Faça um programa que calcule as raízes de uma equação do
# segundo grau, na forma ax2 + bx + c. O programa deverá pedir os
# valores de a, b e c e fazer as consistências, informando ao usuário
# nas seguintes situações:- Se o usuário informar o valor de A igual a zero, a equação não é do
# segundo grau e o programa não deve fazer pedir os demais valores,
# sendo encerrado;
# - Se o delta calculado for negativo, a equação não possui raizes
# reais. Informe ao usuário e encerre o programa;
# - Se o delta calculado for igual a zero a equação possui apenas uma
# raiz real; informe-a ao usuário;
# - Se o delta for positivo, a equação possui duas raiz reais; informe-
# as ao usuário;

import math

a = int(input('Digite o valor de a para a equacao ax2 + bx + c: '))
b = int(input('Digite o valor de b para a equacao ax2 + bx + c: '))
c = int(input('Digite o valor de c para a equacao ax2 + bx + c: '))

if(a == 0):
    print('A equação não é do segundo grau')
else:
    delta_equacao = b ** 2 - 4 * a * c
    if(delta_equacao < 0):
        print(delta_equacao, 'a equação não possui raízes reais.')
    elif(delta_equacao == 0):
        raiz1 = -(b) + (math.sqrt(delta_equacao))/(2 * a)
        print('Delta: %s ' %delta_equacao ,'e raiz real: %s ' %raiz1)
    elif(delta_equacao > 0):
        raiz1 = -(b) + (math.sqrt(delta_equacao)) / (2 * a)
        raiz2 = -(b) - (math.sqrt(delta_equacao)) / (2 * a)
        print('Delta: %s '%delta_equacao,'e raízes reais: %s ' %raiz1 , 'e %s ' %raiz2)
