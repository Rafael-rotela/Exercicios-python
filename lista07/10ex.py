def financiamento(valorEntrada, valorVeiculo, quantidadeParcela, taxaJuros):
    valorFinanciamento = valorVeiculo - valorEntrada
    
    i = taxaJuros
    n = quantidadeParcela
    
    # Fórmula da Tabela Price
    valorParcela = valorFinanciamento * (i * (1 + i)**n) / ((1 + i)**n - 1)
    
    totalPago = valorEntrada + (valorParcela * n)
    totalJuros = totalPago - valorVeiculo
    
    print(f'Total pago: R$ {totalPago:.2f}')
    print(f'Total de juros pago: R$ {totalJuros:.2f}')
    print(f'Valor de cada parcela: R$ {valorParcela:.2f}')


entrada = float(input('Digite o valor de entrada: R$ '))
veiculo = float(input('Digite o valor do veículo: R$ '))
parcelas = int(input('Digite a quantidade de parcelas: '))
juros = float(input('Digite a taxa de juros mensal (ex: 0.02 para 2%): '))

financiamento(entrada, veiculo, parcelas, juros)
