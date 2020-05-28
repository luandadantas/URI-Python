a = 10
b = 20
c = 30

for I in range(0, 20 + 1, 2):
    i_aux = I/10 if I % 10 != 0 else I//10
    a_aux = a/10 if a % 10 != 0 else a//10
    b_aux = b/10 if b % 10 != 0 else b//10
    c_aux = c/10 if c % 10 != 0 else c//10

    print("I={} J={}".format(i_aux,a_aux))
    print("I={} J={}".format(i_aux,b_aux))
    print("I={} J={}".format(i_aux,c_aux))

    a += 2
    b += 2
    c += 2