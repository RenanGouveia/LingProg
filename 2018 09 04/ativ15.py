#15. Faça um programa que leia 5 números e informe a soma e a média dos números.

lista = []
for i in range(5):
    x = int(input('Digite um número'))
    lista.insert(i, x)

media = sum(lista)/5
print('A some é igual a %s' %sum(lista), 'e a média é %s' %media)