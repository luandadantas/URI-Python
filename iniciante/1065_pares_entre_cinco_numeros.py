valor1 = int(input())
valor2 = int(input())
valor3 = int(input())
valor4 = int(input())
valor5 = int(input())

val_list = [valor1, valor2, valor3, valor4, valor5]
val_pares = 0

for valor in val_list:
    if valor % 2 == 0:
        val_pares += 1

print("{} valores pares".format(val_pares))