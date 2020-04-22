valor_total = float(input())
notas = [100, 50, 20, 10, 5, 2]
moedas = [100, 50, 25, 10, 5, 1]

print("NOTAS:")
for nota in notas:
    valor = int(valor_total // nota)
    valor_total = valor_total - (nota * valor)
    print("{} nota(s) de R$ {:.2f}".format(valor, nota))

print("MOEDAS:")
valor_total = round(valor_total * 100)
for moeda in moedas:
    valor = int(valor_total // moeda)
    valor_total = valor_total - (moeda * valor)
    print("{} moeda(s) de R$ {:.2f}".format(valor, moeda/100))
