def troca_de_valores(a,b):
    list_valores[a], list_valores[b] = list_valores[b], list_valores[a]

list_valores = []
for i in range(20):
    list_valores.append(int(input()))

primeiro_valor = 0
ultimo_valor = 19
for i in range(10):
    troca_de_valores(primeiro_valor, ultimo_valor)
    primeiro_valor += 1
    ultimo_valor -= 1

for i in range(20):
    print("N[{}] = {}".format(i,list_valores[i]))