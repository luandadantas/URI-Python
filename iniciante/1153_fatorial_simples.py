N = int(input())

list_num = list(range(N,0,-1))

multip = 1
for i in list_num:
    multip *= i

print(multip)