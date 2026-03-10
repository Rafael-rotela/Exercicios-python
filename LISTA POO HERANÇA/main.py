from Animais import Peixe
from Animais import Cachorro

print("SYS ANIMAL")
print("Qual animal deseja cadastrar")

op = int(input('1 - Peixe, 2 - Cachorro'))

if op != 1 and op != 2:
    print("OPÇÃO INVÁLIDA")
elif op == 1:
    nome = input("Digite o nome do Peixe: ")
    cor = input('Digite o nome do Cor')
    escamas = input('Tem escamas???')
    a1 = Peixe(nome,cor,escamas)
    a1.faz_glu_glu_glu()

elif op == 1:
    nome = input("Digite o nome do Peixe: ")
    cor = input('Digite o nome do Cor')
    raca = input('Qual é a raça do Cachorro???')
    dog = Cachorro(nome,cor,raca)
    dog.latir()
    