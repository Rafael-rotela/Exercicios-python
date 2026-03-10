# SUPERCLASSE
class Animal:
    def __init__(self,nome,color):
        self.nome = nome
        self.color = color
    
    def mover(self):
        print(f'{self.nome} andou')

class Cachorro(Animal):
    def __init__(self, nome, color,raca,rabo=True):
        super().__init__(nome, color)
        self.raca = raca
        self.rabo = rabo

    def mover(self):
        print("ALTERANDO O METODO HERDADO............... POLIMORFISMO")
        print(f'{self.nome}correuuuuuuuuuuuuuu')
    def latir(self):
        print('auauauauauuauauuauauauaua')
class Peixe(Animal):
    def __init__(self, nome, color,escamas=True):
        super().__init__(nome, color)
        self.escamas = escamas
    
    def mover(self):
        print(f'{self.nome} NADOUUUU')
    
    def faz_glu_glu_glu(self):
        print('glu glu glu')

