N = int(input())

for i in range(N):
    num = int(input())
    if num != 0 and num % 2 == 0:
        print("EVEN", end=" ")
    if num % 2 != 0:
        print("ODD", end=" ")
    if num > 0:
        print("POSITIVE")
    if num < 0:
        print("NEGATIVE")
    if num == 0:
        print("NULL")