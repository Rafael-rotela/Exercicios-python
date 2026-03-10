"""
 'self'  se refere a uma pessoa
 __init__ se vc quiser estanciar um objeto
 
"""

class Pessoa:
    def __init__(self, nome, idade, endereco): 
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
    def get_mostrar_nome(self):
        return self.nome
    def set_idade(self,nova_idade):
        self.idade = nova_idade
    def mostrar_cidade(self):
        return self.endereco
    def mostrar_dados(self):
        print(f' nome: {self.nome} \n idade: {self.idade} \n cidade: {self.endereco}')

p1 = Pessoa('Rafael', 18,'Aero Rancho') # p1 é um Objeto da Classe Pessoa
# p1.mostrar_dados() ## p1 é uma instância que pode executar o método mostrar_dados()
p1.set_idade(19)
p1.mostrar_dados()
