A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

if B - C < A < B + C:
    perimetro = A + B + C
    print("Perimetro = {:.1f}".format(perimetro))
else:
    area_trapezio = ((A + B) * C) / 2
    print("Area = {:.1f}".format(area_trapezio))