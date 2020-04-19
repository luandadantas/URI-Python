codigo1, num_peca1, valor_uni1 = input().split(" ")
codigo2, num_peca2, valor_uni2 = input().split(" ")

codigo1 = int(codigo1)
num_peca1 = int(num_peca1)
valor_uni1 = float(valor_uni1)
codigo2 = int(codigo2)
num_peca2 = int(num_peca2)
valor_uni2 = float(valor_uni2)

valor_a_pagar = (num_peca1 * valor_uni1) + (num_peca2 * valor_uni2)

print("VALOR A PAGAR: R$ {:.2f}".format(valor_a_pagar))