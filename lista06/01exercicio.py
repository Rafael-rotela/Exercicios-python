
produto = {'nome': 'Caneta',
           'preco': 2.5,
           'marca':'bic',
           'estoque': 100
           }

for chave,key in produto.items():
    print(f"A chave é: {chave}, e o valor: {key}")

produto['preco'] = 2.9

print("-"*10, 'remover', "-"*10)
print(produto)
for i in range(3):
    chave = input(f"Digite o {i+1}ª que queira retirar: ")
    if i == 2:
        if chave in produto:
            produto.pop(chave)
            print("O produto")
        else:
