lista =  []
while True: 
    numero = int(input('digite um numero: '))
    lista.append(numero)
    if numero < 0:
        break
lista.sort
print(f'o maximo é {max(lista)}e o minimo é {min(lista)}')