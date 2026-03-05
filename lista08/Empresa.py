class Empresa:
    def __init__(self,nome_empresa,cnpj,endereco,qnt_funcionarios,afiliais):
        self.nome_empresa = nome_empresa
        self.cnpj = cnpj
        self.endereco = endereco
        self.qnt_funcionarios = qnt_funcionarios
        self.afiliais = afiliais
    def set_nome_empresa(self, novo_nome):
        self.nome_empresa = novo_nome
    
    def set_cnpj(self,novo_cnpj):
        self.cnpj = novo_cnpj
    
    def set_endereco(self, novo_cnpj): 
        self.endereco = novo_cnpj

    def set_qnt_funcionarios(self,nova_qnt_funcionarios):
        self.qnt_funcionarios = nova_qnt_funcionarios

    def set_afilais(self,nova_afiliais):
        self.afiliais = nova_afiliais
    
    def get_nome_empresa(self):
        return self.nome_empresa 
    
    def get_cnpj(self):
        return self.cnpj 
    
    def get_endereco(self):
        return self.endereco 

    def get_qnt_funcionarios(self):
        return self.qnt_funcionarios

    def get_afilais(self):
        return self.afiliais 
    
