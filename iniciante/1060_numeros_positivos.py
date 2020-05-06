valor1 = float(input())
valor2 = float(input())
valor3 = float(input())
valor4 = float(input())
valor5 = float(input())
valor6 = float(input())

valores_list = [valor1, valor2, valor3, valor4, valor5, valor6]
val_positivos = 0

for valor in valores_list:
    if valor > 0:
        val_positivos = val_positivos + 1

print(str(val_positivos) + " valores positivos")