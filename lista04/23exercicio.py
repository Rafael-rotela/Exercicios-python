numero = int(input('digite um número: '))
soma_divisores= 1
for i in range(1, numero):
    if numero % i == 0:
        soma_divisores += i
print(f"a dos divisores do número {numero}", soma_divisores)
