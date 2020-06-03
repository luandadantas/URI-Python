N = int(input())

for i in range(1, N + 1):
    valor1 = i * i
    valor2 =  i ** 3
    print("{} {} {}".format(i, valor1, valor2))
    print("{} {} {}".format(i, valor1 + 1, valor2 + 1))