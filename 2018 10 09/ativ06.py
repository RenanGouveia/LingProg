#6Defna a função todosnimparesQ que recebe como argumento uma lista de
#números inteiros w e devolve True se w contém apenas números ímpares e False
#em caso contrário.
#Ex: todosnimparesQ([1,3,5,7]) = True


todos_impares = lambda lista: True if len(lista) == 0 or (lista[len(lista)-1]%2 != 0 and todos_impares(lista[:-1])) else False

print(todos_impares([3, 1, 3, 1]))