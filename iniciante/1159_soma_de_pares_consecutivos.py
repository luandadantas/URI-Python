X = 1
while X != 0:
    list_num = []
    X = int(input())

    if X == 0:
        break

    while True:
        if X % 2 == 0:
            list_num.append(X)
        X += 1

        if list_num and len(list_num) == 5:
            break

    soma = sum(list_num)
    print(soma)