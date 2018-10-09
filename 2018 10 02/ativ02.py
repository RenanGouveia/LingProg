#2 Defina a função div que recebe como argumentos dois números naturais m
#e n e devolve o resultado da divisão inteira de m por n. Neste exercício você não
#pode recorrer às operações aritmétcas de multplicação, divisão e resto da divisão
#inteira.

def div(a, b):
    return 0 if a < b else 1 + div(a - b, b)

print(div(10, 5), div(50, 2), div(60, 5), div(51, 7))