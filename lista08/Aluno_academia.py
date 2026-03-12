class Aluno_academia:
    def __init__ (self,nome,idade,peso,altura,mensalidade = 120):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = mensalidade
    def calcular_imc (self):
        calculo = self.peso / self.altura**2
        return calculo
    def obter_valor_mensalidade(self):
        if self.idade >= 18:
            return self.mensalidade
        else:
            desconto = 0.20
            return self.mensalidade/desconto