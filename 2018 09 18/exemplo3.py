class Animal:
    def __init__(self, nome):
        self.nome = nome
        print('Animal sendo criado')
    def quemSouEu(self):
        print(f'Animal {self.nome}')

    def __str__(self):
        return f'Animal {self.nome}'

    def __len__(self):
        return len(self.nome)

    def __del__(self):
        print(f'{self.nome} sendo apagado')


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Cachorro sendo criado")

    def quemSouEu(self):
        print("Cachorro")


a = Animal('Leão')
a.quemSouEu()
