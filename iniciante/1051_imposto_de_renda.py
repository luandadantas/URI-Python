valor_salario = float(input())

taxa_ir1 = 0.08
taxa_ir2 = 0.18
taxa_ir3 = 0.28

if 0 <= valor_salario <= 2000.00:
    print('Isento')
else:    
    if 2000.01 <= valor_salario <= 3000.00:
        valor_nao_isento = valor_salario - 2000.00
        imposto_renda = valor_nao_isento * taxa_ir1
    elif 3000.01 <= valor_salario <= 4500.00:
        ir_parcial1 = 1000.00 * taxa_ir1
        ir_parcial2 = (valor_salario - 3000.00) * taxa_ir2
        imposto_renda = ir_parcial1 + ir_parcial2
    elif valor_salario > 4500.00:
        ir_parcial1 = 1000.00 * taxa_ir1
        ir_parcial2 = 1500.00 * taxa_ir2
        ir_parcial3 = (valor_salario - 4500.00) * taxa_ir3
        imposto_renda = (ir_parcial1 + ir_parcial2 + ir_parcial3)
    print('R$ {:.2f}'.format(imposto_renda))