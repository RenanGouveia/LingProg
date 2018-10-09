#3 Defna a função primnalg que recebe como argumento um número natural e
#devolve o primeiro algarismo (o mais signifcatvo) na representação decimal de n.

def prim_alg(n):
    return n if n < 10 else prim_alg(n//10)

print(prim_alg(6649895), prim_alg(52623264), prim_alg(9522323))