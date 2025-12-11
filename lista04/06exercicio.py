i = 0 
lista = []
while i <= 9:
    num = int(input("Digite um numero: "))
    lista.append(num)
    i += 1
print(f"soma: {sum(lista)}")