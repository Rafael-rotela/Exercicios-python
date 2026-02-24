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
