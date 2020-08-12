X = float(input())
count_N = 0

while True:
    print("N[{}] = {:.4f}".format(count_N,X))
    X = X / 2
    count_N += 1
    if count_N == 100: break