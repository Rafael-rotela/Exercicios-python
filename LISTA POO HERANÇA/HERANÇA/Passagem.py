class Passagem:
    def __init__(self,preco,assento):
        self.preco = preco
        self.assento = assento

    def alterar_preco(self,novo_preco):
        self.preco = novo_preco
        
    def escolher_assento(self, assento_escolhido):
        self.assento = assento_escolhido

class PassagemBus(Passagem):
    def __init__(self, preco, assento,placa,leito):
        super().__init__(preco, assento)
        self.placa = placa
        self.leito = leito

    def abastecer():
        return "Onibus está com tanque cheio"
    
class PassagemAviao(Passagem):
    def __init__(self, preco, assento,portaEmbarque,checkin):
        super().__init__(preco, assento)
        self.portaEmbarque = portaEmbarque
        self.checkin = checkin
    
    def decolar():
        return "Decolou"