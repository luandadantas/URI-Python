N = int(input())
count = 0

while count < N:
    list_num = []
    X, Y = input().split(" ")

    X = int(X)
    Y = int(Y)

    while True:
        if X % 2 == 1:
            list_num.append(X)
        X += 1

        if list_num and len(list_num) == Y:
            break

    soma = sum(list_num)
    print(soma)
    count += 1