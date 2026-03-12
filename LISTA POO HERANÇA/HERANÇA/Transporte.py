class Transporte:
    def __init__(self, capacidade):
        self.capacidade = capacidade

class Aquatico(Transporte):
    def __init__(self, capacidade, tipo_casco):
        super().__init__(capacidade)
        self.tipo_casco = tipo_casco

class Aereo(Transporte):
    def __init__(self, capacidade, altitude_maxima):
        super().__init__(capacidade)
        self.altitude_maxima = altitude_maxima

class Lancha(Aquatico):
    def __init__(self, capacidade, tipo_casco, potencia_motor):
        super().__init__(capacidade, tipo_casco)
        self.potencia_motor = potencia_motor

class Navio(Aquatico):
    def __init__(self, capacidade, tipo_casco, arqueacao_bruta):
        super().__init__(capacidade, tipo_casco)
        self.arqueacao_bruta = arqueacao_bruta

class AviaoMonomotor(Aereo):
    def __init__(self, capacidade, altitude_maxima, tipo_helice):
        super().__init__(capacidade, altitude_maxima)
        self.tipo_helice = tipo_helice

class AviaoComercial(Aereo):
    def __init__(self, capacidade, altitude_maxima, companhia_aerea):
        super().__init__(capacidade, altitude_maxima)
        self.companhia_aerea = companhia_aerea

lancha1 = Lancha(8, "Fibra", "300HP")
lancha2 = Lancha(12, "Alumínio", "450HP")
lancha3 = Lancha(6, "Fibra", "150HP")

navio1 = Navio(2000, "Aço", 50000)
navio2 = Navio(1500, "Aço", 30000)
navio3 = Navio(5000, "Aço Reforçado", 120000)

monomotor1 = AviaoMonomotor(2, 12000, "Passo Fixo")
monomotor2 = AviaoMonomotor(4, 15000, "Passo Variável")
monomotor3 = AviaoMonomotor(2, 10000, "Passo Fixo")

comercial1 = AviaoComercial(180, 40000, "Latam")
comercial2 = AviaoComercial(220, 41000, "Azul")
comercial3 = AviaoComercial(350, 43000, "Gol")

print(f"Lancha 1: {lancha1.capacidade}, {lancha1.tipo_casco}, {lancha1.potencia_motor}")
print(f"Lancha 2: {lancha2.capacidade}, {lancha2.tipo_casco}, {lancha2.potencia_motor}")
print(f"Lancha 3: {lancha3.capacidade}, {lancha3.tipo_casco}, {lancha3.potencia_motor}")

print(f"Navio 1: {navio1.capacidade}, {navio1.tipo_casco}, {navio1.arqueacao_bruta}")
print(f"Navio 2: {navio2.capacidade}, {navio2.tipo_casco}, {navio2.arqueacao_bruta}")
print(f"Navio 3: {navio3.capacidade}, {navio3.tipo_casco}, {navio3.arqueacao_bruta}")

print(f"Monomotor 1: {monomotor1.capacidade}, {monomotor1.altitude_maxima}, {monomotor1.tipo_helice}")
print(f"Monomotor 2: {monomotor2.capacidade}, {monomotor2.altitude_maxima}, {monomotor2.tipo_helice}")
print(f"Monomotor 3: {monomotor3.capacidade}, {monomotor3.altitude_maxima}, {monomotor3.tipo_helice}")

print(f"Comercial 1: {comercial1.capacidade}, {comercial1.altitude_maxima}, {comercial1.companhia_aerea}")
print(f"Comercial 2: {comercial2.capacidade}, {comercial2.altitude_maxima}, {comercial2.companhia_aerea}")
print(f"Comercial 3: {comercial3.capacidade}, {comercial3.altitude_maxima}, {comercial3.companhia_aerea}")