
# 3. Usando a notação com @, implementando os decorators por meio de classes

class Eq:
	def __init__ (self,f3):
		self.f3 = f3
		self.equacoes =[]
	def __call__(self,lista):
		for e in lista:
			self.equacoes.append(self.f3(e))
		return self.equacoes
@Eq
def funcao3(lista):
	eq = str(lista) + "xˆ2" + "+" + str(lista) + "x" + "+"+ str(lista)
	return eq
print(funcao3([5,8,4]))
