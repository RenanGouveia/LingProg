# 2. Usando a notação com @, implementando os decorators por meio de funções

def ordena2(f2):
    def decorator(lista):
        return f2(sorted(lista))

    return decorator


@ordena2
def funcao2(lista):
    print(lista)


print(funcao2([25, 2, 4, 10, 7, 30, 4, 7]))
