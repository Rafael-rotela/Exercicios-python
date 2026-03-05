"""
16) Crie uma função que receba múltiplos argumentos não nomeados, considere que a função receba números flutuantes como argumentos e retorne a média dos argumentos.
"""


def celularOuTv(**kwargs):
    if kwargs['altura'] > kwargs['larguras']:
        return 'celular'
    elif kwargs['larguras'] > kwargs['altura']:
        return 'tv'
tv = {
    'nome' : celularOuTv(),
    'larguras': 100,
    'altura': 70
}
x = celularOuTv(**tv)
print(x)
