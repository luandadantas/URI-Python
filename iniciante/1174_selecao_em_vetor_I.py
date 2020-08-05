indice = 0
while indice != 100:
    valor = float(input())
    if valor <= 10:
        print("A[{}] = {}".format(indice, valor))
    indice += 1