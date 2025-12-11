lista = []
numero = int(input("Digite o tamanho da lista: "))
inicio = int(input("Digite o 1º número: "))
lista.append(inicio)
for i in range(1 , numero):
    numero1 = int(input("Digite o proximo numero: "))
    lista.append(numero1)
print(lista)
print(f"O maior numero é {max(lista)}")