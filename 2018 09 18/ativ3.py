""""

3 Jogo de Blackjack: Faça um joguinho simples em Python.
Aqui estão os requisitos:
- Você precisa criar um jogo de BlackJack (21g baseado em texto simples
- O jogo precisa ter um jogador contra um croupier automatzado.
- O jogador pode desistr ou bater.
- O jogador deve ser capaz de escolher o seu valor de aposta.
- Você precisa acompanhar o dinheiro total do jogador.
- Você precisa alertar o jogador de vitórias, derrotas ou estouros, etc ...

"""
import random, os, sys

cartas = {1: 'ás', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco', 6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove', 10: 'dez',
          11: 'valete', 12: 'rainha', 13: 'rei'}
naipes = {'p': 'paus', 'c': 'copas', 'e': 'espadas', 'o': 'ouro'}
aposta = float(input("Digite quanto deseja apostar:"))
croupier = aposta
jogador = aposta


class Cartas:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return (cartas[self.rank] + " de " + naipes[self.suit])

    def rank(self):
        return (self.rank)

    def naipe(self):
        return (self.suit)

    def arredonda(self):
        if self.rank > 9:
            return (10)
        else:
            return (self.rank)


def mostraMao(hand):
    for Cartas in hand:
        print(Cartas)


def mostraContagem(hand):
    print("Contagem das Cartas: " + str(cartasContagem(hand)))


def cartasContagem(hand):
    cartasContagem = 0
    for Cartas in hand:
        cartasContagem += Cartas.arredonda()
    return (cartasContagem)


def fim(score, money):
    print("Blackjack! *Placar final* croupier: " + str(score['croupier']) + " Você: " + str(score['jogador']))
    print("Saldo Final: croupier: " + str(money['croupier']) + " Você: " + str(money['jogador']))
    sys.exit(0)


deck = []
suits = ['p', 'c', 'e', 'o']
score = {'croupier': 0, 'jogador': 0}
money = {'croupier': croupier, 'jogador': jogador}
hand = {'croupier': [], 'jogador': []}

for suit in suits:
    for rank in range(1, 14):
        deck.append(Cartas(rank, suit))

continuarJogando = True

while continuarJogando:

    random.shuffle(deck)
    random.shuffle(deck)
    random.shuffle(deck)

    hand['jogador'].append(deck.pop(0))
    hand['croupier'].append(deck.pop(0))

    hand['jogador'].append(deck.pop(0))
    hand['croupier'].append(deck.pop(0))

    playjogador = True
    bustedjogador = False

    while playjogador:
        os.system('clear')
        print("Blackjack! croupier: " + str(score['croupier']) + " Você: " + str(score['jogador']))
        print("Saldo jogadores:" + str(money['croupier']) + " Você: " + str(money['jogador']))
        print()

        print('Sua Mão:')

        mostraMao(hand['jogador'])

        mostraContagem(hand['jogador'])

        print()

        inputCycle = True
        userInput = ''

        while inputCycle:
            userInput = input("(C)Continuar , (P)Parar, ou (S)Sair: ").upper()
            if userInput == 'C' or 'P' or 'S':
                inputCycle = False

        if userInput == 'C':

            hand['jogador'].append(deck.pop(0))
            if cartasContagem(hand['jogador']) > 21:
                playjogador = False
                bustedjogador = True
        elif userInput == 'P':
            playjogador = False
        else:
            fim(score, money)
    playcroupier = True
    bustedcroupier = False

    while not bustedjogador and playcroupier:
        print(cartasContagem(hand['croupier']))
        if cartasContagem(hand['croupier']) < 17:
            hand['croupier'].append(deck.pop(0))
        else:
            playcroupier = False

        if cartasContagem(hand['croupier']) > 21:
            playcroupier = False
            bustedcroupier = True

    if bustedjogador:
        print('Você perdeu!')
        money['croupier'] += aposta
        money['jogador'] -= aposta
        score['croupier'] += 1
    elif bustedcroupier:
        print('croupier perdeu')
        money['croupier'] -= aposta
        money['jogador'] += aposta
        score['jogador'] += 1
    elif cartasContagem(hand['jogador']) > cartasContagem(hand['croupier']):
        print('Você Ganhou!')
        money['croupier'] -= aposta
        money['jogador'] += aposta
        score['jogador'] += 1
    elif cartasContagem(hand['jogador']) == cartasContagem(hand['croupier']):
        print('Empate!')
    else:
        print('croupier Ganhou!')
        money['croupier'] += aposta
        money['jogador'] -= aposta
        score['croupier'] += 1

    print()
    print('Mão da Máquina:')
    mostraMao(hand['croupier'])
    mostraContagem(hand['croupier'])

    print()
    print('Sua mão:')
    mostraMao(hand['jogador'])
    mostraContagem(hand['jogador'])
    print()

    if input("Precione (S) para sair ou enter para jogar a próxima rodada").upper() == 'S':
        fim(score, money)
    valorAposta = float(input("Digite um novo valor a ser apostado:"))

    deck.extend(hand['croupier'])
    deck.extend(hand['jogador'])

    del hand['croupier'][:]
    del hand['jogador'][:]




