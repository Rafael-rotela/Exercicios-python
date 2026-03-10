class Funcionario:
    def __init__(self,nome,sobrenome,Horas_trabalhadas,Valor_hora):
        self.nome = nome
        self.sobrenome = sobrenome
        self.Horas_trabalhadas = Horas_trabalhadas
        self.Valor_hora = Valor_hora

    def nomeCompleto(self):
        return f'nome: {self.nome + self.sobrenome} '
    def calcularSalario (self):
        valorTotal = self.Horas_trabalhadas * self.Valor_hora
        return f'Valor total: R${valorTotal}'
    def incrementar_hora(self,incremento_horas):
        self.Horas_trabalhadas = incremento_horas
