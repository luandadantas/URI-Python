T = int(input( ))

for i in range(T):
    list_sequence = [0,1]
    N = int(input())

    if N != 0:
        while len(list_sequence) != N + 1:
            next_number = list_sequence[-2] + list_sequence[-1]
            list_sequence.append(next_number)
        print("Fib({}) = {}".format(N, list_sequence[-1]))
    else:
        print("Fib({}) = 0".format(N))