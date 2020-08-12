count_valor = 0
count_par = 0
list_par = []
count_impar = 0
list_impar = []

while count_valor != 15:
    valor = int(input())

    if valor % 2 == 0:
        list_par.append(valor)
        if len(list_par) == 5:
            for a in list_par:
                print("par[{}] = {}".format(count_par, a))
                count_par +=1
            list_par = []
            count_par = 0

    if valor % 2 == 1:
        list_impar.append(valor)
        if len(list_impar) == 5:
            for a in list_impar:
                print("impar[{}] = {}".format(count_impar, a))
                count_impar +=1
            list_impar = []
            count_impar = 0
    count_valor += 1

if count_valor == 15:
    for a in list_impar:
        print("impar[{}] = {}".format(count_impar, a))
        count_impar +=1
    for a in list_par:
        print("par[{}] = {}".format(count_par, a))
        count_par +=1