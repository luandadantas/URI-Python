N = int(input())

for i in range(N):
    sum_impares = 0
    X, Y = input().split()
    X = int(X)
    Y = int(Y)

    if Y < X:
        X,Y = Y,X
    if X % 2 == 1:
        X += 1
    for i in range(X, Y):
        if i % 2 == 1:
            sum_impares += i
    print(sum_impares)