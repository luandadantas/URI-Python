A, B, C = input().split(" ")

A = int(A)
B = int(B)
C = int(C)

maiorAB = (A + B + abs(A - B)) / 2
maiorAB = int(maiorAB)

if maiorAB > C:
    print(maiorAB,"eh o maior")
else:
    print(C,"eh o maior")    