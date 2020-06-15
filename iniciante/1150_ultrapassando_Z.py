X = int(input())
Z = int(input())

soma = 0
qtd_numeros_list = []

while Z < X or Z == X:
    Z = int(input())

for i in range (X, Z + 1):
    soma = i + soma
    qtd_numeros_list.append(i)

    if soma > Z:
        break

print(len(qtd_numeros_list))