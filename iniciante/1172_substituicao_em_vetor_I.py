list_valores = []
for i in range(10):
    list_valores.append(int(input()))

    if list_valores[-1] <= 0:
        print("X[{}] = 1".format(i))
    else:
        print("X[{}] = {}".format(i,list_valores[-1]))