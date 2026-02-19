def pesca(peso, quantidade):
    if peso > 50:
        peso_excedido = peso - 50
        valorMulta = peso_excedido * 4
        print(f'Você excedeu o valor, e vai ter que pagar o valor de R${valorMulta} com o excesso de {quantidade} peixes')
    else:
        print(f'Não teve que pagar a multa, teve {peso}kg e trouxe {quantidade} de peixes')
pesca(37,7)