#1 Defna a função somannat que recebe como argumento um número natural n
#e devolve a soma de todos os números naturais até n.

def soma_nat(n):
    return 1 if n == 1 else n + soma_nat(n-1)

print(soma_nat(2), soma_nat(3), soma_nat(4), soma_nat(5))