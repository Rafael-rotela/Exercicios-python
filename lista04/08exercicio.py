
lista = []
while len(lista) < 10:
    num = int(input("Digite um numero: "))
    if num > 0:
        lista.append(num)
    else:
        print("apenas numeros positivos! ")
media = sum(lista) / len(lista)
print("a media dos numeros: ", media)