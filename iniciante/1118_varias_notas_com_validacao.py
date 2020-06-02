notas_list = []
sair = False

while not sair:
    nota = float(input())

    if nota < 0 or nota > 10:
        print("nota invalida")
    if 0 <= nota and nota <= 10:
        notas_list.append(nota)
    if len(notas_list) == 2: 
        media = sum(notas_list) / 2
        print("media = {:.2f}".format(media))
        notas_list = []

        X = 0
        while X != 1 and X != 2:
            X = int(input("novo calculo (1-sim 2-nao)\n"))
            if X == 1:
                continue
            if X == 2: 
                sair = True