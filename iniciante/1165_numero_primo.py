N = int(input())
count_n = 0

while count_n != N:
    list_num_perfeito = []
    X = int(input())
    
    for i in range (1, X+1):
        if X % i == 0:
            list_num_perfeito.append(i)

    if sum(list_num_perfeito) == X + 1:
        print("{} eh primo".format(X))
    else:
        print("{} nao eh primo".format(X))

    count_n += 1