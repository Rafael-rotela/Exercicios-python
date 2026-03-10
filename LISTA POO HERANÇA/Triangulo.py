class Triangulo:
    def __init__(self,ladoA,ladoB,ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB 
        self.ladoC = ladoC

    def calcular_Perimetro(self):
        perimetro = self.ladoC + self.ladoB + self.ladoA
        return perimetro
