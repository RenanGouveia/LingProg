# 3. Escreva uma função que exibe uma lista recebida como parâmetro. Ela deve,
# contudo, ordenar a lista antes. A ordenação deve ser feita por meio de um
# decorator.


# 1. Sem usar a notação com @

def ordena(f):
    def decorator(lista):
        return f(sorted(lista))

    return decorator


def funcao(lista):
    print(lista)


funcao = ordena(funcao)
print(funcao([4, 3, 4, 7, 1, 15, 1, 7]))
