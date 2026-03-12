class Ingresso:
    def __init__(self,preco,setor):
        self.preco = preco
        self.setor = setor

    def alterar_preco(self,novo_preco):
        self.preco = novo_preco

    def mostrar_setor(self):
        return self.setor
    
class IngressoVIP(Ingresso):
    def __init__(self, preco, setor,camarote:bool,open_bar:bool,open_fod:bool,estacionamento:bool):
        super().__init__(preco, setor)
        self.camarote = camarote
        self.open_bar = open_bar
        self.open_food = self.open_food
        self.estacionamento = estacionamento

    def ativar_openFood_E_openBar(self):
        self.open_bar = True
        self.open_food = True

    def Desativar_openFood_E_openBar(self):
        self.open_bar = False
        self.open_food = False

    def pegar_bebida(self):
        return 'pegou bebida'
    def acessar_camarote(self):
        self.camarote = True
        return self.camarote