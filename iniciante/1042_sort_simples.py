A, B, C = input().split()

A = int(A)
B = int(B)
C = int(C)

valores_crescentes_list = [A, B, C]
valores_crescentes_list.sort()
ordem_original = [A, B, C]

for i in valores_crescentes_list:
    print(i)
print()
for i in ordem_original:
    print(i)