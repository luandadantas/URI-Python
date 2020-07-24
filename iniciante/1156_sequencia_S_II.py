S = 1
x = 1

for i in range(3,39,2):
    x *= 2
    valor = i/x
    S += valor

print("{:.2f}".format(S))