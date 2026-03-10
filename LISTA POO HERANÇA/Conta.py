class Conta:
    def __init__(self,nome:str,cpf:str,numero:int,saldo = 0):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo

    def depositar(self,novo_deposito):
        self.saldo = novo_deposito

    def sacar (self, valor_saque):

        novo_saldo = self.saldo

        if self.saldo > 0:
            saque = novo_saldo - valor_saque
            self.saldo - saque
            return f'Seu saque foi de {saque}'
        else:
            return 'Não á valor a ser sacado.'
        
    def Imprimir_saldo(self):
        return f'saldo = R${self.saldo}'