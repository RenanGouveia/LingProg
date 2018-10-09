#7 Defna a função pertenceQ que recebe como argumentos uma lista de números
#inteiros w e um número inteiro n e devolve True se n ocorre em w e False em
#caso contrário.
#Ex: pertenceQ([1,2,3],1) = True
#x: pertenceQ([1,2,3],2) = True
#Ex: pertenceQ([1,2,3],3) = True
#Ex: pertenceQ([1,2,3],4) = False


def pertence(lista, numero, i):
    if not lista[i:]:
        return False
    if lista[i] == numero:
        return True
    return(pertence(lista, numero, i+1))

print(pertence([2, 6, 5, 8], 10, 0))