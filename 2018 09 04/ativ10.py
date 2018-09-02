#10. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
#quantas notas de cada valor serão fornecidas. As notas disponíveis
#serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a
#quantidade de notas existentes na máquina.
#- Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#- Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece
## três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.


saque = int(input('Informe o valor que deseja sacar: Notas disponíveis: 1, 5, 10, 50 e 100 reais'))

if(saque<10 or saque>600):
    print('Valor mínimo 10 reais e máximo 600 reais.')
elif(saque < 50 and saque >= 10):
    nota_dez = saque//10
    resto_dez = saque%10
    nota_cinco = resto_dez//5
    resto_cinco = resto_dez%5
    nota_um = resto_cinco//1
    resto_um = resto_cinco%1
    print('',nota_dez, 'Notas de R$10\n',nota_cinco, 'Notas de R$5\n',nota_um,' Notas de R$1')
elif(saque >= 50 and saque <= 100):
    nota_cinquenta = saque//50
    resto_cinquenta = saque%50
    nota_dez = resto_cinquenta//10
    resto_dez = resto_cinquenta%10
    nota_cinco = resto_dez//5
    resto_cinco = resto_dez%5
    nota_um = resto_cinco//1
    resto_um = resto_cinco%1
    print('',nota_cinquenta,'Notas de R$50\n',nota_dez,'Notas de R$10\n',nota_cinco,'Notas de R$5\n',nota_um,'Notas de R$1')
else:
    nota_cem = saque//100
    resto_cem = saque%100
    nota_cinquenta = resto_cem//50
    resto_cinquenta = resto_cem%50
    nota_dez = resto_cinquenta//10
    resto_dez = resto_cinquenta%10
    nota_cinco = resto_dez//5
    resto_cinco = resto_dez%5
    nota_um = resto_cinco//1
    resto_um = resto_cinco%1
    print('',nota_cem,'Notas de R$100\n',nota_cinquenta,'Notas de R$50\n',nota_dez,'Notas de R$10\n',nota_cinco,'Notas de R$5\n',nota_um,'Notas de R$1')