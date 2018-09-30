
class Pessoa:
    contador = 0
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Pessoa.contador += 1

p1 = Pessoa("Renan", 21)
print(Pessoa.contador)
p2 = Pessoa("Renanzinho", 22)
print(Pessoa.contador)

print(p1.contador, ' : ', p1.nome,', tem ', p1.idade, 'anos.')
print(p2.contador, ' : ', p2.nome,', tem ', p2.idade, 'anos.')