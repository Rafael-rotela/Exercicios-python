"""
 'self'  se refere a uma pessoa
 __init__ se vc quiser estanciar um objeto
 
"""



class Pessoa:
    def __init__(self, nome, idade, cidade): 
        self.nome = nome
        self.idade = idade
        self.cidade =cidade
    def mostrar_dados(self):
        print(f' nome: {self.nome} \n idade: {self.idade} \n cidade: {self.cidade}')

p1 = Pessoa('Rafael', 18,'Campo Grande') # p1 é um Objeto da Classe Pessoa
p1.mostrar_dados() ## p1 é uma instância que pode executar o método mostrar_dados()

p2 = Pessoa('IZA',15,'Campo Grande')
p2.mostrar_dados()