
"""
Crie a classe Linha que tem dois atributos, coordenada1 e coordenada2.
Cada coordenada é uma tupla que carrega duas coordenadas cartesianas (x,y) que
denotam pontos do segmento de reta. Faça métodos que calculem o comprimento
do segmento de reta e sua inclinação.

"""


class Linha:
    def __init__(self, coordenada1, coordenada2):
        self.coordenada1 = coordenada1
        self.coordenada2 = coordenada2

def calculo():

    x1 = int(input(f'Digite o valor de x1: '))
    y1 = int(input(f'Digite o valor de y1: '))
    x2 = int(input(f'Digite o valor de x2: '))
    y2 = int(input(f'Digite o valor de y2: '))

    coordenada1 = (x1, y1)
    coordenada2 = (x2, y2)

    try:
        horizontal = coordenada2[1] - coordenada1[1]
        vertical = coordenada2[0] - coordenada1[0]

        comprimento = ((horizontal ** 2) + (vertical ** 2) ** (1/2))

        print('Inclinação da Reta: ', horizontal/vertical, 'Comprimento: ', comprimento)
    except IOError:
        print('Não deu certo')
    finally:
        print('Finally deu certo')

calculo()
