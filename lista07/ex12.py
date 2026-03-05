"""
12 - Crie uma função que receba uma lista como argumento, os valores da lista devem ser numéricos, por fim retorne a média desses valores.
"""
numeros = [2,3,4,5,6,7,8,9,10]
def mediaLista(lista):
    media = 0
    for soma in lista:
        media += soma
    print( media / len(lista))

mediaLista(numeros)