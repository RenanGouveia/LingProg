#12. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#Morango
#Maçã
#Até 5 Kg
#R$ 2,50 por Kg
#R$ 1,80 por Kg
#Acima de 5 Kg
#R$ 2,20 por Kg
#R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da
#compra ultrapassar R$ 25,00, receberá ainda um desconto de 10%
#sobre este total. Escreva um algoritmo para ler a quantidade (em
#Kg) de morangos e a quantidade (em Kg) de maças adquiridas e
#escreva o valor a ser pago pelo cliente.

kg_maca = float(input('Kg de Maça: '))
kg_morango = float(input('Kg de Morango: '))

if(kg_maca <= 5):
    valor_maca = kg_maca * 2.50
elif(kg_maca > 5):
    valor_maca = kg_maca * 2.20

if(kg_morango <=5):

    valor_morango = kg_morango * 1.80

elif(kg_morango > 5):
    valor_morango = kg_morango * 1.50

total = valor_maca + valor_morango

if(total > 25 or (kg_morango + kg_maca) >= 8):
    desconto = total * 0.1
    print('Total: %s ' %(total - desconto),'. Desconto de %s '%desconto)
else:
    desconto = 0.0
    print('Total: %s ' %(total - desconto),'. Desconto de %s '%desconto)
