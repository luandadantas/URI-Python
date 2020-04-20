dist_tot_perc = int(input())
tot_comb_gasto = float(input())

consumo_medio = dist_tot_perc / tot_comb_gasto

print("{:.3f}".format(consumo_medio), "km/l")