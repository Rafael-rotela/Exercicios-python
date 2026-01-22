print('-' * 10, "ELEIÇÃO", '-' * 10)

print("""
Candidatos:
1 - Pedro
2 - Caio
3 - João
4 - Rafael
5 - Voto Nulo
6 - Voto em Branco
0 - Sair
""")


Pedro = Caio = João = Rafael = 0
VotoNulo = VotoEmBranco = 0
votos_totais = 0

while True:
    try:
        voto = int(input("Digite o número do candidato: "))
    except ValueError:
        print("Digite um número válido!")
        continue

    if voto == 0:
        print("Votação encerrada.")
        break
    elif voto == 1:
        Pedro += 1
        votos_totais += 1
    elif voto == 2:
        Caio += 1
        votos_totais += 1
    elif voto == 3:
        João += 1
        votos_totais += 1
    elif voto == 4:
        Rafael += 1
        votos_totais += 1
    elif voto == 5:
        VotoNulo += 1
        votos_totais += 1
    elif voto == 6:
        VotoEmBranco += 1
        votos_totais += 1
    else:
        print("Opção inválida!")
        VotoNulo += 1 


if votos_totais > 0:
    porcentagem_nulo = (VotoNulo / votos_totais) * 100
    porcentagem_branco = (VotoEmBranco / votos_totais) * 100
else:
    porcentagem_nulo = porcentagem_branco = 0

candidatos_votos = {
    "Pedro": Pedro,
    "Caio": Caio,
    "João": João,
    "Rafael": Rafael
}

maior_voto = max(candidatos_votos.values())

ganhadores = []
for nome, votos in candidatos_votos.items():
    if votos == maior_voto and votos > 0:
        ganhadores.append(nome)


print(f"""
========= RESULTADO DA ELEIÇÃO =========

Pedro:  {Pedro}
Caio:   {Caio}
João:   {João}
Rafael: {Rafael}

Votos nulos: {VotoNulo}
Votos em branco: {VotoEmBranco}

Porcentagem de votos nulos: {porcentagem_nulo:.2f}%
Porcentagem de votos em branco: {porcentagem_branco:.2f}%
""")

if len(ganhadores) == 0:
    print("Não houve ganhador.")
elif len(ganhadores) == 1:
    print(f"Ganhador da eleição: {ganhadores[0]} com {maior_voto} votos")
else:
    print(f"Houve empate entre: {', '.join(ganhadores)} com {maior_voto} votos")
