#Escreva uma função que calcula a soma dos n primeiros números naturais, dado
#que n é recebido como parâmetro. Escreva um decorator que garanta que o valor
#recebido é natural (maior ou igual a 1).


# 1. Sem usar a notação com @
def valida (f):
	def soma_n_primeiros(n):
		if (n>=1):
			return f(n)
		else:
			print("Menor que 1")
			return 0
	return soma_n_primeiros
def outra_funcao(n):
	soma=0
	for x in range(n+1):
		soma = soma + x
	return soma

outra_funcao = valida(outra_funcao)
print(outra_funcao(6))
print(outra_funcao(-3))

