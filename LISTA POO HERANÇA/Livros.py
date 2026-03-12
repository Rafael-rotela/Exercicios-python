class Livro:
    def __init__(self,nome,autor,editora,paginas,descricao,dimensao:tuple,idioma):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas
        self.idioma = idioma
        self.dimensao = dimensao
        self.descricao = descricao

    def Alterar_editora(self,nova_editora):
        self.editora = nova_editora
    def Listar_qnt_paginas(self):
        return self.paginas
    def set_descricao(self,nova_descricao):
        self.descricao = nova_descricao
    def set_dimensao(self,nova_dimensao):
        self.dimensao = nova_dimensao
    def set_nome(self,novo_nome):
        self.nome = novo_nome
    def set_comprimtento(self,novo_cumprimento,nova_largura,nova_profundidade):
        self.dimensao = (novo_cumprimento,nova_profundidade,nova_largura)
    def get_todasInformacao(self):
        return (f"""
        nome: {self.nome}
        autor: {self.autor}
        editora: {self.editora}


        quantidade de paginas: {self.paginas}
        idioma: {self.idioma}
        dimensão:{self.dimensao[0]} x {self.dimensao[1]} x {self.dimensao[2]}

        descrição:
        {'='*50}
        {self.descricao}
        {'='*50}
        """)    