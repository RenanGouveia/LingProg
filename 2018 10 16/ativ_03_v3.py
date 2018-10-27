
# 3. Usando a notação com @, implementando os decorators por meio de classes


class Ordena:
    def __init__(self, f3):
        self.f3 = f3

    def __call__(self, lista):
        return self.f3(sorted(lista))


@Ordena
def funcao3(lista):
    print(lista)


print(funcao3([10, 50, 4, 20, 3, 150, 6, 22]))