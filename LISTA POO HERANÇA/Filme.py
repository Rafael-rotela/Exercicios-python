class Filme:
    def __init__(self,nome,duracao):
        self.nome = nome
        self.duracao = duracao
    def play(self):
        return f'{self.nome} foi iniciado'
    
class Acao(Filme):
    def __init__(self, nome, duracao,):
        super().__init__(nome, duracao)

    def explodir(self):
        return 'Expludir'
    
class Comedia(Filme):
    pass