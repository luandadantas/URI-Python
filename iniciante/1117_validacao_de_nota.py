notas_list = []

while len(notas_list) < 2:
    nota = float(input())
    if 0 > nota or nota > 10:
        print("nota invalida")
    else:
        notas_list.append(nota)

soma = sum(notas_list)
divisao = soma / 2
print("media = {:.2f}".format(divisao))