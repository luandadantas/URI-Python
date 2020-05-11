I = 1
J = 60

while True:
    print("I={} J={}".format(I, J))
    I = I + 3
    J = J - 5
    if J < 0:
        break