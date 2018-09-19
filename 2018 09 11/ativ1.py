def f (a, b):
    if a%2 == 0 and b%2 == 0:
        if a >= b: 
            return b
        else: 
            return a
    else:
        if a >= b:
            return a
        else:
            return b

print(f(1, 2)) 
print(f(2, 6))
print(f(4, 6))
