num = int(input("digite um numero: "))
div =1 
lista_divisores = []

while div < num:
    if num % div == 0:
        lista_divisores.append(div)
        div += 1
print(lista_divisores)
print(sum(lista_divisores))