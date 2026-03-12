class Carro:
    def __init__(self,marca,cor,ano,valor,consumo,nivel=0):
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.consumo = consumo
        self.nivel = nivel
    def abastecer(Self, novo_nivel):
            print(Self.nivel)
            Self.nivel = novo_nivel
    def anadar(self):
         