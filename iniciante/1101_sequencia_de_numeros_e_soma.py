M = 1
N = 1

while M > 0 and N > 0:
    numeros_int_list = []
    numeros_str_list = []
    M, N = input().split()
    M = int(M)
    N = int(N)

    if M > N:
        M,N = N,M

    for i in range(M,N+1):
        numeros_int_list.append(i)
        soma = sum(numeros_int_list)
        string_i = str(i)
        numeros_str_list.append(string_i)

    if M <= 0 or N <= 0:
        break
    else:
        juntar_val = " ".join(numeros_str_list)
        print("{} Sum={}".format(juntar_val, soma))