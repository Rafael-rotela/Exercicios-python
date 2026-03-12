class Compra:
    def __init__(self, numero, produto, valor):
        self.numero = numero
        self.produto = produto
        self.valor = valor
        self.valor_total = 0

    def calcular_valor_total(self):
        icms = self.valor * 0.17
        frete = self.valor * 0.05
        self.valor_total = self.valor + icms + frete
        return self.valor_total

class Avista(Compra):
    def __init__(self, numero, produto, valor, desconto):
        super().__init__(numero, produto, valor)
        self.desconto = desconto

    def preco_com_desconto(self):
        total_com_taxas = self.calcular_valor_total()
        valor_final = total_com_taxas - (total_com_taxas * (self.desconto / 100))
        return valor_final

class Parcelada(Compra):
    def __init__(self, numero, produto, valor, num_parcelas):
        super().__init__(numero, produto, valor)
        self.num_parcelas = num_parcelas

    def valor_das_parcelas(self):
        total_com_taxas = self.calcular_valor_total()
        return total_com_taxas / self.num_parcelas