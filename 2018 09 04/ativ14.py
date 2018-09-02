#14. Faça um programa que leia 5 números e informe o maior número.

lista = []
for i in range(5):
    x = int(input('Digite um número'))
    lista.insert(i, x)

lista.sort()
lista.reverse()
print('O maior da lista: %s' %lista, 'é o %s' %lista[0])