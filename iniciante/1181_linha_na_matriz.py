linha = int(input())
T = input()
list_matriz = []
l_operacao = []

for i in range(12):
    list_linha = []
    for j in range(12):
        valor = float(input())
        list_linha.append(valor)
    list_matriz.append(list_linha)

l_operacao = list_matriz[linha]

if T == "S":
    print(f"{sum(l_operacao):.1f}")
if T == "M":
    print(f"{(sum(l_operacao))/12:.1f}")