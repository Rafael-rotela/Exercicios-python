class Imovel:
    def __init__(self, inscricao_municipal, valor_aluguel, iptu):
        self.inscricao_municipal = inscricao_municipal
        self.valor_aluguel = valor_aluguel
        self.iptu = iptu

    def obter_parcela_iptu(self):
        return self.iptu / 12

    def set_valor_aluguel(self, novo_valor):
        self.valor_aluguel = novo_valor

class Casa(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, tem_piscina, tem_churrasqueira):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.tem_piscina = tem_piscina
        self.tem_churrasqueira = tem_churrasqueira

class Condominio(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, area_lazer, portaria_24h):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.area_lazer = area_lazer
        self.portaria_24h = portaria_24h

class Apartamento(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, num_quartos, tem_elevador):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.num_quartos = num_quartos
        self.tem_elevador = tem_elevador

class Terreno(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, area_m2, eh_murado):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.area_m2 = area_m2
        self.eh_murado = eh_murado

class Chacara(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, tem_pomar, area_hectares):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.tem_pomar = tem_pomar
        self.area_hectares = area_hectares