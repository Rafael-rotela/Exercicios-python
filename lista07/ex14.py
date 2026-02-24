energia = 55000
tempo = 1
valor = 2.50


def calcularValor(energiaFunc, tempoLigado):
    return (energiaFunc * tempoLigado)/1000
def valorKwh(func, valorKwh):
    return func * valorKwh

consumo = calcularValor(energia, tempo)

print(valorKwh(consumo, valor))