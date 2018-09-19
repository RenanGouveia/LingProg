def blackjack (a, b, c):
    cartas = a + b + c
    if cartas <= 21:
        return cartas
    else:
        if 11 in [a, b, c]:
            return cartas - 10
        return ('Estourou', cartas)

print(blackjack(1, 11, 8))
print(blackjack(0, 11, 0))
print(blackjack(1, 11, 20))