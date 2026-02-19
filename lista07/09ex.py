def calcularTempo(tempo):
    pis = 0.033
    cofins = 0.02
    icms = 0.17
    
    if tempo <= 15:
        return 'Sem taxa'
    
    if tempo <= 60:
        return 'Valor R$ 9.00'
    
    horas = tempo // 60
    valor = 9.00 + (horas - 1) * 1.5
    
    valor_pis = valor * pis
    valor_cofins = valor * cofins
    valor_icms = valor * icms
    imposto = valor_pis + valor_cofins + valor_icms
    total = valor + imposto
    
    return f"""
Tempo: {tempo} minutos
PIS: R$ {valor_pis:.2f}
COFINS: R$ {valor_cofins:.2f}
ICMS: R$ {valor_icms:.2f}
Total de impostos: R$ {imposto:.2f}
Total com impostos: R$ {total:.2f}
"""

print(calcularTempo(120))

