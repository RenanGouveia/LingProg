
# 2. Escreva uma função que recebe uma lista de triplas e, para cada uma, gera uma
# equação do segundo grau considerando que os elementos da tripla são os
# coefcientes usualmente denominados a, b e c da equação. Note que a sua função
# deverá devolver uma lista de equações. A geração das equações deve ser feita por
# meio de, evidentemente, decorators.

# 1. Sem usar a notação com @

def recebe_f(f):
	equacoes = []
	def decorator(lista):
		for e in lista:
			equacoes.append(f(e))
		return equacoes 
	return decorator
def funcao(lista):
	eq = str(lista) + "xˆ2" + "+" + str(lista) + "x" + "+"+ str(lista)
	return eq
funcao = recebe_f(funcao)
print(funcao([5,7,2]))

