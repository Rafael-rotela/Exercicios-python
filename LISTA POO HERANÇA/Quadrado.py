class Quadrado:
    def __init__(self,lado):
        self.lado =lado
        
    def get_lado(self): ## OBTER O VALOR DO LADO
        return self.lado
    
    def set_lado(self,novo_lado): ## ATRIBUIR UM VALOR AO LADO
        self.lado = novo_lado
    
    def calcular_area(self): ## CALCULAR
        area = self.lado * self.lado
        return area
    

q1 = Quadrado(2)
q2 = Quadrado(4)
q3 = Quadrado(6)
q4 = Quadrado(8)
q5 = Quadrado(10)

area_q3 = q3.calcular_area()
print(area_q3)

print(q4.get_lado())
print('AREA DO Q4:')