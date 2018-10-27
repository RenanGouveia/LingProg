def cria_decorator(funcao):
    #def decorator():
    #   print("Testando Decorator enganador.")
        #funcao()
    return lambda: funcao()
    return decorator
@cria_decorator
def funcao_a_ser_decorada():
    print("Função a ser decorada.")

funcao_a_ser_decorada()