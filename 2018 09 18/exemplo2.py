class Livro:
    def __init__(self, titulo, numero_paginas):
        self.titulo = titulo
        self.numero_paginas = numero_paginas
        self.aberto = False

    def abrir(self):
        self.aberto = True

    def fechar(self):
        self.aberto = False


l = Livro ('Python, como programar?', 500)
print('Livro: ', l.titulo, '| Páginas: ', l.numero_paginas)