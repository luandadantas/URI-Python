N = int(input())

for i in range(N):
    valor1, valor2, valor3 = input().split()
    valor1 = float(valor1)
    valor2 = float(valor2)
    valor3 = float(valor3)

    media_ponderada = (valor1 * 2 + valor2 * 3 + valor3 * 5) / 10
    print("{:.1f}".format(media_ponderada))