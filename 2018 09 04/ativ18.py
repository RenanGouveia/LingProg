#18. A série de Fibonacci é formada pela seqüência
#1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série
#até o n−ésimo termo.

termo = int(input('Digite o valor do n-ésimo termo: '))

def fibonacci (n):
    a, b = 0 ,1

    while (b < n):
        print(b)
        a, b = b, a+b

fibonacci(termo)