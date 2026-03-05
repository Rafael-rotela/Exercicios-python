#churrascaria 
"""
18 – Uma rede de churrascaria realiza promoções semanais e precisa automatizar os descontos de acordo com o dia da semana (terça-feira 10%, quarta-feira 15%, quinta-feira 20%). Crie uma função que calcule o preço final do consumo por pessoa.
Considere a taxa de atendimento e o couvert, caso o cliente concorde com o pagamento. Utilize argumentos nomeados **kwargs, Exemplo de chamada da função:
desconto(‘quinta-feira’,valor=99.90,taxa=0.10,couvert=15)
"""

def desconto(dia,**kwargs):
    produto_final = 0
    desconto = 0

    if dia =='terça-feira':
        desconto = 1.10
    if dia =='quarta-feira':
        desconto = 1.15
    if dia =='quinta-feira':
        desconto = 1.20

    produto = (kwargs['valor']+kwargs['taxa']+kwargs['couvert'])
    produto_final = (kwargs['valor'] * desconto) + (kwargs["couvert"] + kwargs['taxa'])
    return f"""
        conta s/ taxas: {produto}
        Conta C/ Taxas: 
         Rodízios: {produto}
         Taxas Serviços: {kwargs['taxa']}
         Couvert: {kwargs['couvert']}
         TOTAL: R$ {produto_final}
        """    

x = desconto('quinta-feira',valor=99.90,taxa=0.10,couvert=15)
print(x)