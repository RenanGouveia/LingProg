
# 2. Usando a notação com @, implementando os decorators por meio de funções

def valida2 (f2):
	def soma_n_primeiros2(n):
		if (n>=1):
			return f2(n)
		else:
			print("Menor que 1")
			return 0
	return soma_n_primeiros2

@valida2
def outra_funcao2(n):
	soma=0
	for x in range(n+1):
		soma = soma + x
	return soma

print(outra_funcao2(4))
print(outra_funcao2(-5))
