"""
11 - Crie uma função que receba como argumento uma lista, com 
valores de qualquer tipo. A função deve imprimir todos os 
elementos da lista numerando-os. Exemplo:
1, Pera
2, Uva
3, Maça
4, Salada mista
"""
carrinho = ['Pera', 'Uva','Maça','Salada mista']

def listagem(lista):
    for numero, produto in enumerate(lista):
        print(numero ,'-', produto)

listagem(carrinho)
