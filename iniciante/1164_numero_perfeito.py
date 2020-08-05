N = int(input())
count_n = 0

while count_n != N:
    list_num_perfeito = []
    X = int(input())
    
    for i in range(1, X):
        if X % i == 0:
            list_num_perfeito.append(i)
    
    if sum(list_num_perfeito) == X:
        print("{} eh perfeito".format(X))
    else:
        print("{} nao eh perfeito".format(X))

    count_n += 1