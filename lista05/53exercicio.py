print('*'*10, 'BemMaisFort', '-'*10)

i = 0
grupo = []

while True:
    pessoa = {
        'idade': int(input('digite sua idade: ')),
        'sexo': input('digite seu sexo (M/F): ').lower(),
        'altura': float(input('digite sua altura: ')),
        'peso': float(input('digite seu peso: '))
    }

    grupo.append(pessoa)
    i += 1

    if i == 2:
        break

pesos = [p['peso'] for p in grupo]
print('O maior peso é:', max(pesos))

idades = [p['idade'] for p in grupo]
print('A maior idade é:', max(idades))

alturas = [p['altura'] for p in grupo]
print('A maior altura é:', max(alturas))
print('A menor altura é:', min(alturas))
