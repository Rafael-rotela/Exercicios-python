def calcular_salario(horas_trabalhadas, valor_hora):
    if horas_trabalhadas <= 40:
        salario = horas_trabalhadas * valor_hora
    else:
        hora_extra = horas_trabalhadas - 40
        salario_normal = 40 * valor_hora
        salario_extra = hora_extra * valor_hora * 1.5
        salario = salario_normal + salario_extra
        
    return salario


# Exemplo de uso
horas = 45
valor = 20

total = calcular_salario(horas, valor)
print("Salário a receber: R$", total)
