# Parametro nomeados -------------->> nome  = 'Rafael'

def cadastro_cnh(**kwargs):
    print(kwargs)
    if kwargs['idade'] >= 18:
        return True
    else:
        return False
    
x = cadastro_cnh(nome = 'Thiago', idade=15,sexo='M')
print(x)