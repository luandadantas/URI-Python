X = list(map(int, input().split(" ")))
A = X.pop(0)
A_list = []

for i in X:
    if i > 0:
        N = i
        break

for i in range(0, N):
    A1 = A + i
    A_list.append(A1)

soma_A = sum(A_list)
print(soma_A)