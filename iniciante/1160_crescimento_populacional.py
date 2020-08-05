def crescimento_populacao(populacao, percentual):
    crescimento = (populacao * percentual) / 100
    return crescimento

T = int(input())
count = 0

while count != T:
    PA, PB, G1, G2 = input().split(" ")

    PA = int(PA)
    PB = int(PB)
    G1 = float(G1)
    G2 = float(G2)
    anos = 0

    while PA <= PB:
        PA = int(crescimento_populacao(PA, G1) + PA)
        PB = int(crescimento_populacao(PB, G2) + PB)
        anos += 1

        if anos > 100:
            break
    
    if anos > 100:
        print("Mais de 1 seculo.")
    else:
        print("{:.0f} anos.".format(anos))
    count += 1