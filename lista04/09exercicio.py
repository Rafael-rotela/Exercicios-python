numero = int(input("Digite um número: "))
maior = numero
menor = numero

i = 1  # já lemos o primeiro número, então começamos do 1

while i < 10:
    numero = int(input("Digite um número: "))

    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

    i += 1

print("Maior número:", maior)
print("Menor número:", menor)
