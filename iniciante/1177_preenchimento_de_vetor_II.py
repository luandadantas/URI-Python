T = int(input())
list_numeros = list(range(0, T))
count = 0

while True:
    for a in list_numeros:
        print("N[{}] = {}".format(count, a))
        count += 1
        if count == 1000: break
    if count == 1000: break