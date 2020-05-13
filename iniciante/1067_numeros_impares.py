X = int(input())
valor = 1

while True:
    if valor % 2 == 1:
        if valor > X:
            break
        print(valor)
        valor += 1
    else:
        valor += 1