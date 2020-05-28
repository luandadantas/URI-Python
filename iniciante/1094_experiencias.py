N = int(input())

total = 0
total_coelho = 0
total_rato = 0
total_sapo = 0

for i in range(N):
    quant_cobaias, tipo_cobaias = input().split()
    quant_cobaias = int(quant_cobaias)

    total += quant_cobaias
    
    if tipo_cobaias == 'C':
        total_coelho += quant_cobaias
    if tipo_cobaias == 'R':
        total_rato += quant_cobaias
    if tipo_cobaias == 'S':
        total_sapo += quant_cobaias

percentual_C = total_coelho * 100 / total 
percentual_R = total_rato * 100 / total
percentual_S = total_sapo * 100 / total

print((
    "Total: {} cobaias\n"
    "Total de coelhos: {}\n"
    "Total de ratos: {}\n"
    "Total de sapos: {}\n"
    "Percentual de coelhos: {:.2f} %\n"
    "Percentual de ratos: {:.2f} %\n"
    "Percentual de sapos: {:.2f} %"
).format(total, total_coelho, total_rato, total_sapo, percentual_C, percentual_R, percentual_S))