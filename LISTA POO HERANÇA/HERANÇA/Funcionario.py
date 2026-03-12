class Funcionario:
    def __init__(self,nome,matricula,salario):
        self.nome = nome 
        self.matricula = matricula
        self.salario = salario 
    def bater_ponto():
        return True

class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario,meta:bool,comissao:float):
        super().__init__(nome, matricula, salario)
        self.meta = meta
        self.comissao = comissao
  
    def bater_meta(self):
        salario_bruto = self.salario
        if self.meta == True:
            salario_bruto = self.salario * self.comissao
            return salario_bruto
        else:
            return salario_bruto

class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario,senha):
        super().__init__(nome, matricula, salario)
        self.senha = senha

