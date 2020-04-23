codigo, quantidade = input().split()

codigo = int(codigo)
quantidade = int(quantidade)

tabela_precos = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}

valor_a_pagar = quantidade * tabela_precos[codigo]
print("Total: R$ {:.2f}".format(valor_a_pagar))