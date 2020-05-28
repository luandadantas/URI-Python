numeros = []

for i in range(1, 100 + 1):
    num = int(input())
    numeros.append(num)

maior = max(numeros)
indice = numeros.index(maior)
print(maior)
print(indice+1)