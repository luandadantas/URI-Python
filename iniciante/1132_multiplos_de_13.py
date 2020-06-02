X = int(input())
Y = int(input())

multiplos_list = []

if Y < X:
    X, Y = Y, X

for i in range(X, Y+1):
    if i % 13 != 0:
        multiplos_list.append(i)
print(sum(multiplos_list))    