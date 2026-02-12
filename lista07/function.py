def hello(nome):
    print(f'Olá, {nome}')
def pintar_de_azul():
    print('Pintando a bolinha de azul')

name = input('Digite seu nome: ')

hello(name)
pintar_de_azul()

def hello(nome = 'Vitor', idade = 0):
    print(f'Olá {nome}, sua idade é {idade}')
def hello0(nome:str, idade:int): #Orienta o usuario
    print(f'Olá {nome}, sua idade é {idade}')

hello('Rafael',19)
hello('Igor',23)



def soma (n1,n2):
    rst = n1 +n2
    return rst
def sub (n1,n2):
    rst = n1 - n2
    return rst
def divi (n1,n2):
    rst = n1 / n2
    return rst
def multiplicacao (n1,n2):
    rst = n1 * n2
    return rst
resultado_soma = soma(19,11)
print(resultado_soma)
print(sub(18,9))
print(divi(9,3))
print(multiplicacao(8,7))


