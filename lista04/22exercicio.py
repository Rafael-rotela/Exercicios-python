i = True
lista = []

while True:
    n = int(input('digite sua nota (caso queira sair digite true): '))
    lista.append(n)
    if  n.lower() == "false":
        break

nota = float(n)

if n > 0:
    media = sum(lista) / len(lista)
    print('A media é: ',media)
else:
    print('digite a tua media.')