#22. O Sr. Manoel Joaquim expandiu seus negócios para além dos
#negócios de 1,99 e agora possui uma loja de conveniências. Faça
#um programa que implemente uma caixa registradora rudimentar.
#O programa deverá receber um número desconhecido de valores
#referentes aos preços das mercadorias. Um valor zero deve ser
#informado pelo operador para indicar o fnal da compra. O programa
#deve então mostrar o total da compra e perguntar o valor em
#dinheiro que o cliente forneceu, para então calcular e mostrar o
#valor do troco. Após esta operação, o programa deverá voltar ao
#ponto inicial, para registrar a próxima compra. A saída deve ser
#conforme o exemplo abaixo:

#Lojas Tabajara
#Produto 1: R$ 2.20
#Produto 2: R$ 5.80
#Produto 3: R$ 0
#Total: R$ 9.00
#Dinheiro: R$ 20.00
#Troco: R$ 11.00
#...

lista_produto = []
lista_compra = []
lista_valor = []
i = 0
def compra():
    global i
    while True:
        produto = str(input('Digite o Produto: '))
        if (produto == '0'): break
        valor = float(input('Digite o valor: '))
        lista_produto.insert(i, produto)
        lista_valor.insert(i, valor)
        i = i + 1
    total()

def total():
    lista_compra = [lista_produto, lista_valor]
    total = sum(lista_valor)
    for i in range(len(lista_produto)):
        print(i, lista_produto[i], ':' 'R$', lista_valor[i])

    print('Total: R$ %s' % total)
    dinheiro = float(input('Insira o dinheiro recebido: '))
    troco = dinheiro - total
    print('Troco: R$ %s' %troco)

    print('NOVA COMPRA:')
    compra()
compra()
