coluna = int(input())
T = input()
list_matriz = []
c_operacao = []

for i in range(12):
    list_linha = []
    for j in range(12):
        valor = float(input())
        list_linha.append(valor)
    list_matriz.append(list_linha)

for a in range(12):
    for b in range(12):
        if b == coluna:
            c_operacao.append(list_matriz[a][b])

if T == "S":
    print(f"{sum(c_operacao):.1f}")
if T == "M":
    print(f"{(sum(c_operacao))/12:.1f}")