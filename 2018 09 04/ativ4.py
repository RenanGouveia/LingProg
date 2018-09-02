# 4. Faça um Programa que leia três números e mostre-os em ordem decrescente.

lista = []

for i in range(3):
    x = int(input('Digite um número: '))
    lista.insert(i, x)

lista.reverse()
print(lista)

