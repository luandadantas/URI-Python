valor = int(input())
list_valores = [valor]

for i in range(10):
    print("N[{}] = {}".format(i, valor))
    valor = valor * 2
    list_valores.append(valor)