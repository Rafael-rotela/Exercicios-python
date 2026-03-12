class Carro:
    def __init__(self,modelo,marca,cor,ano,valor,consumo,nivel=0):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano 
        self.valor = valor
        self.consumo = consumo
        self.nivel = nivel
    def set_abastecer(self, novo_nivel):
        self.nivel = novo_nivel
    def set_andar(self):
        self.