def tem_33(lista):
    status = "Nada"
    for simbolo in lista:
        if simbolo == 3:
            if status == "Nada":
                status = "Tres"
            elif status == "Tres":
                return True
        else:
            if status == "Tres":
                status = "Nada"
    return False

tem_33([2, 3, 5, 3, 8, 3, 3])