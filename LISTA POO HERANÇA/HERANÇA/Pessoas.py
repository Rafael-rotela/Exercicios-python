class Pessoa:
    def __init__(self,matricula,nome,idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade

    def set_nome(self,novo_nome):
        self.nome = novo_nome
    def get_nome(self):
        return self.nome
    
    def set_idade(self,nova_idade):
        self.idade = nova_idade
    def get_idade(self):
        return self.idade

    def get_matricula(self):
        return self.matricula

class Professor(Pessoa):
    def __init__(self, matricula, nome, idade,formacao,disciplina,carga_horaria,salario,):
        super().__init__(matricula, nome, idade)
        self.formacao = formacao
        self.disciplina = disciplina
        self.carga_horaria = carga_horaria
        self.salario = salario


    def set_formacao(self,nova_formacao):
        self.nova_formacao = nova_formacao


class Aluno(Pessoa):
    def __init__(self, matricula, nome, idade,nota1,nota2,nota3,nota4,estudar:bool):
        super().__init__(matricula, nome, idade)
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        self.estudar = estudar

    def definir_media(self):
        calculo = (self.nota1 +self.nota2 +self.nota3 +self.nota4)/4
        return calculo
