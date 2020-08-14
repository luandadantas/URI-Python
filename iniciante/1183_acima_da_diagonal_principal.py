operacao = input()
list_matriz = []
list_operacao = []

for i in range(12):
    list_linha = []
    for j in range(12):
        valor = float(input())
        list_linha.append(valor)
    list_matriz.append(list_linha)

for a in range(12):
    for b in range(12):
        if b > a:
            list_operacao.append(list_matriz[a][b])

if operacao == "S":
    print(f"{sum(list_operacao):.1f}")
if operacao == "M":
    print(f"{(sum(list_operacao))/len(list_operacao):.1f}")