lista = []
soma = 0 
numero = int(input("digite um número de 100 a 9999"))
if (numero<100 or numero>9999):
    print("Número invalido")
else:
    numero = str(numero)
    for num in numero:
        lista.append(num)
print("Os algorismos são ", lista)