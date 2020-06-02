total_grenais = 0
vitorias_inter = 0
vitorias_gremio = 0
empates = 0
X = 0

while X != 2:
    inter, gremio = input().split()
    inter = int(inter)
    gremio = int(gremio)
    total_grenais += 1

    if inter > gremio:
        vitorias_inter += 1
    if gremio > inter:
        vitorias_gremio += 1
    if inter == gremio:
        empates += 1

    X = int(input("Novo grenal (1-sim 2-nao)\n"))

print("{} grenais".format(total_grenais))
print("Inter:{}".format(vitorias_inter))
print("Gremio:{}".format(vitorias_gremio))
print("Empates:{}".format(empates))

if inter > gremio:
    print("Inter venceu mais")
if gremio > inter:
    print("Gremio venceu mais")