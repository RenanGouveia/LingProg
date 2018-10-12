#8 Defna a função junta que recebe como argumentos duas listas de números
#inteiros w1 e w2 e devolve a concatenação de w1 com w2 .
#Ex: junta([1,2,3],[4,5,6]) = [1, 2, 3, 4, 5, 6]
#Ex: junta([],[4,5,6]) = [4, 5, 6]
#Ex: junta([1,2,3],[]) = [1, 2, 3]


juncao = lambda lista1,lista2: lista1+lista2


print(juncao([1,2,3],[4,5,6]))