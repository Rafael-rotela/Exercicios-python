####### ATRIBUTO OU MÉTODO PRIVADO, SOMENTE A PROPRÍA CLASS PODE ACESSAR

class Retangulo:
    def __init__(self,base,altura):
        self.base = base ## PUBLICO
        self.__altura = altura ## PRIVADO

    def get_base(self):
        return self.base
    def get_altura(self):
        return self.__altura
    
    def calcular_area(self):
        return self.base * self.__altura
    
rt1 = Retangulo(8,10)
print(rt1.base)
print(rt1.calcular_area())