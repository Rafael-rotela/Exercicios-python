class Agenda:
    def __init__(self,dia,mes,ano,anatocao):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = anatocao

    def validar_data(self):
        return f'{self.dia/self.mes/self.ano}'
    def set_anotar_tarefa(self, nova_anotacao):
        self.anotacao = nova_anotacao
    def mostrar_anotacao(self):
        return self.anotacao