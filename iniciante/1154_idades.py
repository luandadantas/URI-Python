idade = 0
list_idades = []

while idade >= 0:
    idade = int(input())
    if idade >= 0:
        individuos = list_idades.append(idade)

media = sum(list_idades) / len(list_idades)
print("{:.2f}".format(media))