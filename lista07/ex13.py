"""
13) Crie uma função que retorne uma lista com valor padrão. Para esta função, consideraremos como argumentos de entrada a quantidade de elementos e o valor padrão a ser atribuído a todos eles. Exemplo de retorno:
[1,1,1,1,1,1,1,1]
[“A”,”A”,”A”,”A”]
"""


def funcao(quantidade,  valor, *wargs):
    lista = []
    for i in range(quantidade):
        lista.append(valor)
    return lista 
x = funcao(8,1)
print(x)