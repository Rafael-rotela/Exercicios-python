try:
    entrada = int(input('Quantos numero deseja digitar: '))
    lista = []

    for i in range(entrada):
        numero = int(input(f'digite o numero {i}ª: '))
        lista.append(numero)
    print(f"a soma dos teus numero é {sum(lista)} e os numeros são: ")

    j = 0

    while j  < len(lista):
        print('numero: ', lista[j])
        j += 1 
except ValueError:
    print("Erro! Somente numeros inteiros!")