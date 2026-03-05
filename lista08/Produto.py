class Produto:
    def __init__(self) -> None:
        self.nome = ""
        self.preco = 0
        self.tipo = ""
    def mostrar_dados(self):
        print(f' Nome: {self.nome} \n Preço: {self.preco} \n Tipos: {self.tipo} \n')

prod1 = Produto()
print(prod1)
print(prod1.preco)

prod1.preco = 50
print(prod1.preco)

prod2 = Produto()

prod2.nome ='DERTERGENTE'
prod2.preco = 25
prod2.tipo = 'LIMPEZA'

prod2.mostrar_dados()