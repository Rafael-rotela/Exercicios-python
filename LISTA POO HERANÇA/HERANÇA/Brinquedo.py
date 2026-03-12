class Brinquedo:
    def __init__(self, nome, cor, tamanho, preco):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco

    def brincar(self):
        print(f"estou brincando com {self.nome}")

class Buzz(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, voa=True):
        super().__init__(nome, cor, tamanho, preco)
        self.voa = voa

class Woody(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, laca=True):
        super().__init__(nome, cor, tamanho, preco)
        self.laca = laca

class Jessie(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, chapeu=True):
        super().__init__(nome, cor, tamanho, preco)
        self.chapeu = chapeu

class Rex(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, bracos_curtos=True):
        super().__init__(nome, cor, tamanho, preco)
        self.bracos_curtos = bracos_curtos

class Slinky(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, mola_comprimento=2.0):
        super().__init__(nome, cor, tamanho, preco)
        self.mola_comprimento = mola_comprimento

class Porquinho(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, tipo_moeda="Real"):
        super().__init__(nome, cor, tamanho, preco)
        self.tipo_moeda = tipo_moeda

class SrBatata(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, pecas_extras=10):
        super().__init__(nome, cor, tamanho, preco)
        self.pecas_extras = pecas_extras

class Bullseye(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, veloz=True):
        super().__init__(nome, cor, tamanho, preco)
        self.veloz = veloz

class Barbie(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, profissao="Modelo"):
        super().__init__(nome, cor, tamanho, preco)
        self.profissao = profissao

class Zurg(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, nivel_vilania=10):
        super().__init__(nome, cor, tamanho, preco)
        self.nivel_vilania = nivel_vilania