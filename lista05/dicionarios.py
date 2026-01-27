aluno = {
    'aluno01' : 'Rafa',
    'aluno02' : 'Gustavo',
    'aluno03' : 'KILL',
    'aluno04' : 'FABIO'
}

for chaves in aluno.keys():
    print(chaves)

for aluno in aluno.values():
    print(aluno)

for chave,valor in aluno.items():
    print(f'{chave}, Nome: {valor}') 