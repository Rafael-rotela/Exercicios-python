numeros = [12,51,80,46,12,31,17,15,16,17,19]
pares = []
impares = []

for i in numeros:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print('Pares: ', pares)
print('Impares: ', impares)
