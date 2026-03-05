"""
14 – Crie uma função que receba como argumento a potência elétrica de determinado aparelho e o tempo ligado e retorne o consumo em KWh em seguida chame outra função para calcular a conta de energia, levando em consideração o consumo e o valor do KWh como argumentos. Em seguida, chame uma outra função para calcular o valor da conta de acordo com o consumo calculado.
"""



energia = 55000
tempo = 1
valor = 2.50


def calcularValor(energiaFunc, tempoLigado):
    return (energiaFunc * tempoLigado)/1000
def valorKwh(func, valorKwh):
    return func * valorKwh

consumo = calcularValor(energia, tempo)

print(valorKwh(consumo, valor))