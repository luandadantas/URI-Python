X = int(input())
qts_num_impares = 0

while True:
    if X % 2 == 1:
        print(X)
        X +=1
        qts_num_impares += 1
        if qts_num_impares == 6:
            break
    else:
        X +=1