#5 Defna a função contemnparQ que recebe como argumento uma lista de números
#inteiros w e devolve True se w contém um número par e False em caso contrário.
#Ex: contemnparQ([2,3,1,2,3,4]) = True
#Ex: contemnparQ([1,3,5,7]) = False

def contem_par(lista, i=0):
    return False if len(lista)==0 or lista[len(lista)-1]%2 !=0 and not contem_par(lista[:-1]) else True

print(contem_par([5, 6, 7]))

