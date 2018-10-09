#4 Defna a função prod_lista que recebe como argumento uma lista de inteiros e
#devolve o produto dos seus elementos.
#Ex: prod_lista([1,2,3,4,5,6]) = 720

def prod_lista(lista, i =0):
    return lista[i] if len(lista) == 1 else lista[len(lista) -1] * prod_lista(lista[:-1])


print(prod_lista([1, 6, 2, 3]))
