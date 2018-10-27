
# 2. Usando a notação com @, implementando os decorators por meio de funções

def recebe_f2(f2):
	equacoes = []
	def decorator2(lista):
		for e in lista:
			equacoes.append(f2(e))
		return equacoes
	return decorator2

@recebe_f2
def funcao2(lista):
	eq = str(lista) + "xˆ2" + "+" + str(lista) + "x" + "+"+ str(lista)
	return eq
print(funcao2([8,9,3]))


