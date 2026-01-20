"""
lista = []
soma = 0 
while True:
    numero = float(input('Digite o numero(caso queira sair 0): '))
    if numero == 0:
        print("saiu do codigo")
        break 
    lista.append(numero)
print('A soma do numero: ', sum(lista))
print('A quantidade de numero: ', len(lista))
print('A soma do numero: ', sum(lista)/ len(lista))
print(f'o maior numero digitado é {max(lista)} e o numero minimo {min(lista)}')
    
for num in lista:
    if num % 2 == 0:
        soma += num
        print('a media dos pares é: ', soma/num )
    else:
        break
print("A media dos pares é ")
"""

soma = 0 
qnt_numero = 0
media_num = 0
maior = 0 
menor = 0
media_pares = 0 

numero = float(input('quantos numeros você deseja digitar: '))
i = 0 
while i < numero:
    if numero == 0:
        break 
    else:
        print('a')
        i += 1
    