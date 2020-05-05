salario_atual = float(input())

if 0 <= salario_atual <= 400.00:
    percentual_reajuste = '15 %'
    reajuste_ganho = salario_atual * 0.15
    novo_salario = salario_atual + reajuste_ganho
elif 400.01 <= salario_atual <= 800.00:
    percentual_reajuste = '12 %'
    reajuste_ganho = salario_atual * 0.12
    novo_salario = salario_atual + reajuste_ganho
elif 800.01 <= salario_atual <= 1200.00:
    percentual_reajuste = '10 %'
    reajuste_ganho = salario_atual * 0.10
    novo_salario = salario_atual + reajuste_ganho
elif 1200.01 <= salario_atual <= 2000.00:
    percentual_reajuste = '7 %'
    reajuste_ganho = salario_atual * 0.07
    novo_salario = salario_atual + reajuste_ganho 
elif salario_atual > 2000.00:
    percentual_reajuste = '4 %'
    reajuste_ganho = salario_atual * 0.04
    novo_salario = salario_atual + reajuste_ganho 

print('Novo salario: {:.2f}'.format(novo_salario))
print('Reajuste ganho: {:.2f}'.format(reajuste_ganho))
print('Em percentual:', percentual_reajuste)