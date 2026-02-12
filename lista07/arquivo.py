try:
    idade = int(input("Digite sua idade: "))
except:
    print('apenas numeros!!')

def banco(saque, saldo):
    if saque > saldo:
        print('Não há valor suficiente para realizar o saque')
        return saldo
    else:
        return saldo - saque

saldo_atual = banco(10, 20)
print(saldo_atual)

#agendamento de consulta

data = int(input('Escolha a data(número 1 a 31): '))
try:
    c = int(input('Digite a temperatura em Celsius: '))
    conversao = c * 1.8 + 32
    print('Temperatura em Fahrenheit: ', conversao)
except:
    print('ERRO: digite um valor numérico')

#5
try:
    conta = int(input('Valor total da conta: R$'))
    pessoas = int(input('Valor de pessoa na mesa'))
    conta_total = conta / pessoas
    print('Conta:  R$',conta_total)
except ValueError:
    print('Número de pessoas inválido para divisão da conta')

with open('meu_arquivo.txt', 'w', encoding='utf-8') as arquivo:
    conteudo = arquivo.write("Olá")

with open('./meu_arquivo.txt', 'r' , encoding='utf-8') as arq:
    leitor = arq.read()
print(conteudo)
print(leitor)
