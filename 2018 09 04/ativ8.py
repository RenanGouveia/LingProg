# 8. Faça um Programa que peça os 3 lados de um triângulo. O
# programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é:
# equilátero, isósceles ou escaleno.
# Dicas:
# - Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# - Triângulo Equilátero: três lados iguais;
# - Triângulo Isósceles: quaisquer dois lados iguais;
# - Triângulo Escaleno: três lados diferentes;

triangulo = []

for i in range(3):
    lado = int(input('Lado: %s ' % i))
    triangulo.insert(i, lado)

if ((sum(triangulo[0:1]) > triangulo[2]) or (sum(triangulo[1:2]) > triangulo[0]) or ((triangulo[0] + triangulo[2]) > triangulo[1])):
    print('É um triângulo')

    if (triangulo[0] == triangulo[1] and triangulo[1] == triangulo[2]):
        print('Triângulo equilátero')
    elif (triangulo[0] == triangulo[1] or triangulo[1] == triangulo[2] or triangulo[0] == triangulo[2]):
        print('Triângulo isósceles')
    else:
        print('Triângulo escaleno')

else:
    print('Não podem formar um triângulo: %s ' % triangulo[:len(triangulo)])

