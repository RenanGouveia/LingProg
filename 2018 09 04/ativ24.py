#24. Faça um programa que receba o valor de uma dívida e mostre
#uma tabela com os seguintes dados: valor da dívida, valor dos juros,
#quantidade de parcelas e valor da parcela.
#Os juros e a quantidade de parcelas seguem a tabela abaixo:
#Quantidade de Parcelas % de Juros sobre o valor inicial da dívida

#1 - 0
#3 - 10
#6 - 15
#9 - 20
#12 - 25

#Valor da Dívida Valor dos Juros Quantidade de Parcelas Valor da Parcela
#R$ 1.000,00     0               1                       R$ 1.000,00
#R$ 1.100,00     100             3                       R$ 366,00
#R$ 1.150,00     150             6                       R$ 191,67


valor_inicial = float(input('Valor da dívida: '))

total_final = []
valor_divida = []
valor_juros = []
quantidade_parcela = []
valor_parcela = []
parcela = 1
i = 0

while(parcela <= 12):
    if(parcela == 1):
        valor = valor_inicial
        valor_divida.insert(i, valor)
        valor_juros.insert(i, 0)
        quantidade_parcela.insert(i, parcela)
        valor_parcela.insert(i, valor_inicial)
    elif(parcela == 3):
        valor = valor_inicial + (valor_inicial * 0.10)
        valor_divida.insert(i, valor)
        valor_juros.insert(i, (valor - valor_inicial))
        quantidade_parcela.insert(i, parcela)
        valor_parcela.insert(i, (valor/parcela))
    elif(parcela == 6):
        valor = valor_inicial + (valor_inicial * 0.15)
        valor_divida.insert(i, valor)
        valor_juros.insert(i, (valor - valor_inicial))
        quantidade_parcela.insert(i, parcela)
        valor_parcela.insert(i, (valor / parcela))
    elif(parcela == 9):
        valor = valor_inicial + (valor_inicial * 0.20)
        valor_divida.insert(i, valor)
        valor_juros.insert(i, (valor - valor_inicial))
        quantidade_parcela.insert(i, parcela)
        valor_parcela.insert(i, (valor / parcela))
    else:
        valor = valor_inicial + (valor_inicial * 0.25)
        valor_divida.insert(i, valor)
        valor_juros.insert(i, (valor - valor_inicial))
        quantidade_parcela.insert(i, parcela)
        valor_parcela.insert(i, (valor / parcela))

    if(parcela == 1): parcela = 0
    parcela += 3
    i +=1

total_final = [valor_divida, valor_juros, quantidade_parcela, valor_parcela]
print('Vl Div | Vl Juros | Qtde Parc. | Vl Parc.')
for i in range(5):
    print(valor_divida[i],' | ', valor_juros[i],' | ', quantidade_parcela[i],' | ',valor_parcela[i])








