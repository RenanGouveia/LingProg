
# 3. Usando a notação com @, implementando os decorators por meio de classes

class Validar:
	def __init__(self,f3):
		self.f3 = f3
	def __call__(self,n):
		if (n>=1):
			return self.f3(n)
		else:
			print("Menor que 1")
			return 0
@Validar
def outra_funcao2(n):
	soma=0
	for x in range(n+1):
		soma = soma + x
	return soma

print(outra_funcao2(8))
print(outra_funcao2(-8))