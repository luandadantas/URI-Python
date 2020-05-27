X = int(input())
Y = int(input())

if X > Y:
    X, Y = Y, X

soma = 0
for i in range(X + 1, Y):
    if i % 2 != 0:
        soma += i
print(soma)