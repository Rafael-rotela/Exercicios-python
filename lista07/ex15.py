"""
15  Crie uma função que receba múltiplos argumentos não nomeados, considere que a função receba números inteiros como argumentos e retorne a soma dos argumentos.
"""


def somar(*args):
    return sum(args)
x = somar(2,3,4,5,6,7,8,9)
print(x)