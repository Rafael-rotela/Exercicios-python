class NotaFiscal:

    def __init__(self, numero, tipo, serie, cnpj, razao_social, data,valor_produtos, icms, frete, ipi):
        
        self.numero = numero
        self.tipo = tipo  
        self.serie = serie
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.data = data
        self.valor_produtos = valor_produtos
        self.icms = icms
        self.frete = frete
        self.ipi = ipi
        self.valor_total = 0

    def obterNumero(self):
        return self.numero

    
    def obterDataEmissao(self):
        return self.data

    # alterarRazaoSocial()
    def alterarRazaoSocial(self, nova_razao):
        self.razao_social = nova_razao

    # calcularValorTotal()
    def calcularValorTotal(self):
        self.valor_total = self.valor_produtos + self.frete + self.icms + self.ipi
        return self.valor_total