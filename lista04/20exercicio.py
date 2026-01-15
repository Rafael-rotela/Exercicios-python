limitador = int(input('digite o valor maximo que deseja: '))
i = 0
numeroPar = 0
numeroImpar = 0
if  limitador == 0:
    while i <= limitador:
        if i % 2 == 0:
            numeroPar += 1 
        else:
            numeroImpar += 1
        i +=1 
    print(f"""
        numero par: {numeroPar}
        numero impar: {numeroImpar}
    """)
else:
    print('Processo terminado')