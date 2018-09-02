#25. Faça um programa que mostre os n termos da Série a seguir:
#S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
#Imprima no fnal a soma da série.

termo = int(input('Digite o valor do n-ésimo termo: '))
lista = []
def fibonacci (n):
    a, b = 0 ,1
    i = 1
    index = 0
    while (b < n):
        print(i, b)
        lista.insert(index, i/b)
        a, b = b, a+b
        i+=1

fibonacci(termo)
print(lista)
print('Soma: %s' %(sum(lista)))