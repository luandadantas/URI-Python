idade_em_dias = int(input())

ano = idade_em_dias // 365
resto_ano = idade_em_dias % 365
mes = resto_ano // 30
dia = resto_ano % 30

print(str(ano) + " ano(s)")
print(str(mes) + " mes(es)")
print(str(dia) + " dia(s)") 