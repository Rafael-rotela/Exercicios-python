"""
17 – Crie uma função que armazene os dados de uma pessoa em um dicionário e imprima-os na tela, Utilize argumentos nomeados **kwargs, exemplo de saída:
"""

def nomear(**kwargs):
    nome = kwargs['nome'].split()
    email = kwargs['email']
    idade = kwargs['idade']
    pais = kwargs['pais']

    return f"""
        nome: {nome[0]}
        sobrenome: {nome[1]}
        email: {email}
        país: {pais}
        idade: {idade}
        """
print(nomear(nome ='rafael rotela de jesus victor', email = 'rafael341@gmail.com', idade = 20, pais = 'Brasil'))