def somaImposto(custo = 0 , taxaImposto =  1 ):
    taxa = custo * taxaImposto/100
    return  custo - taxa

valor = somaImposto(199,25)
print(valor)