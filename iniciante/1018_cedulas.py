valor = int(input())
cedulas = [100, 50, 20, 10, 5, 2, 1]
print(valor)

for cedula in cedulas:
    nota = valor // cedula
    resto = valor % cedula
    valor = resto
    print(str(nota) + " nota(s) de R$ " + str(cedula) + ",00")