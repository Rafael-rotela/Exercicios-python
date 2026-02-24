carrinho = ['Pera', 'Uva','Maça','Salada mista']

def listagem(lista):
    for numero, produto in enumerate(lista):
        print(numero ,'-', produto)

listagem(carrinho)
