class Contato:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    def __str__(self):
        return f'Contato: {self.nome} e {self.numero}'

def cadastro_contato():
    menu = '1 - Cadastrar\n2 - Listar\n0 - Sair\n'
    op = int(input(menu))
    while op != 0:
        if op == 1:
            try:
                f = open('agenda.txt', 'a')
                nome = input('Digite o nome')
                numero = input('Digite o número')
                f.write(nome + ";" + numero + '\n')
                f.close()
            except IOError:
                print('Não deu certo')
            finally:
                pass
                print('Realmente passou por aqui')
        elif op == 2:
            try:
                contatos = []
                with open('agenda.txt', 'r') as f:
                    linhas = f.readlines()
                    for linha in linhas:
                        partes = linha.split(";")
                        contato = Contato(partes[0], partes[1])
                        contatos.append(contato)
                for contato in contatos:
                    print(contato)

            except IOError:
                pass
            finally:
                print('Finally passando')

        else:
            print('Tchau')
        op = int(input(menu))

cadastro_contato()