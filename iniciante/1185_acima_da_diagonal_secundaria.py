operacao = input()
list_matriz = []
list_operacao = []
matriz = 12

for i in range(matriz):
    list_linha = []
    for i in range(matriz):
        valor = float(input())
        list_linha.append(valor)
    list_matriz.append(list_linha)

for a in range(matriz):
    for b in range(matriz):
        if a + b + 1 == matriz:
            break
        list_operacao.append(list_matriz[a][b])

if operacao == "S":
    print(f"{sum(list_operacao):.1f}")
if operacao == "M":
    print(f"{sum(list_operacao)/len(list_operacao):.1f}")