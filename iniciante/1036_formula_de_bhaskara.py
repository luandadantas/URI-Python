A, B, C = input().split(" ")

A = float(A)
B = float(B)
C = float(C)

bhaskara = B ** 2 - 4 * A * C

if A == 0 or bhaskara < 0:
    print("Impossivel calcular")
else:
    x1 = (- B + bhaskara ** 0.5) / (2 * A) 
    x2 = (- B - bhaskara ** 0.5) / (2 * A) 
    print("R1 = {:.5f}".format(x1))
    print("R2 = {:.5f}".format(x2))