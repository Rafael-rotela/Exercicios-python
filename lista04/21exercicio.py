inicio = int(input('digite o inicio: '))
fim = int(input('digite o inicio: '))

soma_pares = 0
mult_impares = 0
primeiro_impar = 0

if inicio > fim:
    for contador in range(inicio, fim + 1):
        if contador % 2 == 0:
            numeroPar += 1
        else:
            if primeiro_impar:
                mult_impares = contador
                primeiro_impar = False
            else:
                mult_impares *= contador

print('Soma dos números pares: ', soma_pares)
print('Multiplicação dos números ímpares: ', mult_impares)