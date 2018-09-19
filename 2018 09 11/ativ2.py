
def comecam_com_a_mesma_letra(palavra):
    partes = palavra.split(" ")
    return True if partes[0][0] == partes[1][0] else False

    