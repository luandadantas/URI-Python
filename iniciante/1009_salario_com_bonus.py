vendedor = input()
salario_fixo = float(input())
total_vendas = float(input())

comissão = total_vendas * 15 / 100
TOTAL = salario_fixo + comissão

print("TOTAL = R$ {:.2f}".format(TOTAL))