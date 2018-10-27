def cria_hello_decorator(funcao):
    def hello_decorator():
        print("Antes...")
        funcao()
        print("Depois...")
    return hello_decorator

def hello_decorators():
    print("Hello, Decorators.")

hello_decorators = cria_hello_decorator(hello_decorators)
hello_decorators()