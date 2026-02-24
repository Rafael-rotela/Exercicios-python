
numeros = [2,3,4,5,6,7,8,9,10]
def mediaLista(lista):
    media = 0
    for soma in lista:
        media += soma
    print( media / len(lista))

mediaLista(numeros)