class Triangulo:
    def __init__ (self, ladoA,ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
    def calcular_perimetro (self):
        return self.ladoB + self.ladoA
    def get_maiorLado(self):
        if (self.ladoA > self.ladoB):
            return f"Lado maior é {self.ladoA}"
        else:
            return f"Lado maior é {self.ladoB}"