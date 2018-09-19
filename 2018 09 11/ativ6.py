
def f(numeros):
    status = 'Nada'
    for simbolo in numeros:
        if simbolo == 0:
            if status == 'Nada':
                status = 'Zero'
            elif status == 'Zero':
                status = 'Zero1'
        else:
            if simbolo == 7:
                if status == 'Zero1':
                    print('true')
                    return True

    print(status)
    return False

f([1, 7, 3, 0, 0, 3, 7]) 
