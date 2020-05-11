valor1 = float(input())
valor2 = float(input())
valor3 = float(input())
valor4 = float(input())
valor5 = float(input())
valor6 = float(input())

final_list = []

for valor in [valor1, valor2, valor3, valor4, valor5, valor6]:
    if valor >= 0:
        final_list.append(valor)
        media = sum(final_list) / len(final_list)

print("{} valores positivos".format(len(final_list)))
print("{:.1f}".format(media))