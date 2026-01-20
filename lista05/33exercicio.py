numeros = [11,12,13,14,15,16,17,18]

num = int(input('Digite um número: '))

i= 0

while i < len(numeros):
    if num == numeros[i]:
        print(f"{num} está na lista")
        break
    i += 1 