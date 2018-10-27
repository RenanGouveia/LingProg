import time
def cria_decorator_timer(funcao):
    def decorator_timer():
        t0 = time.time()
        funcao()
        return time.time() - t0
    return decorator_timer

@cria_decorator_timer
def funcao_demorada():
    for i in range(10):
        print(i)
        time.sleep(2)

print(funcao_demorada.__name__)