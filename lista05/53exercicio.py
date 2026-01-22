print('-'*10,'BemMaisFort','-'*10)
i = 0


grupo = []

while True:
    pessoa = {
        'idade' : int(input('digite sua idade')),
        'Sexo' : input('digite seu sexo (M/F):').lower(),
        'Altura' : float(input('digite sua altura: ')),
        'Peso' : float(input('digite sua peso:'))
    }
    print('novo cadastro')
    grupo.append(pessoa)
    i += 1
    if i == 2:
        break
pesos = [p['peso'] for p in grupo]
print('O maior peso é: ', max(pesos))