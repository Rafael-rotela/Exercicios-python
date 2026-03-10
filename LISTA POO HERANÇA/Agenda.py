class Agenda:
    def __init__(self,dia,mes,ano,anatocao):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anatocao = anatocao

    def validar_data(self):
        return self.dia, '/', self.mes, '/', self.ano
    def anotar_tarefa(self):
        return self.anatocao