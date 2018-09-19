def f(palavra):
    return " ".join(sorted(palavra.split(" "), reverse=True))

print(f('Estou em casa'))
print(f('Teste do Renan'))