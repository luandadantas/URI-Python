hora_ini, min_ini, hora_fin, min_fin = input().split()

hora_ini = int(hora_ini)
min_ini = int(min_ini)
hora_fin = int(hora_fin)
min_fin = int(min_fin)

if hora_ini > hora_fin:
    duração_parcial_hora = 24 - hora_ini
    duração_total_hora = duração_parcial_hora + hora_fin
elif hora_fin > hora_ini:
    duração_total_hora = hora_fin - hora_ini
elif hora_ini == hora_fin:
    duração_total_hora = 24
    
if min_ini > min_fin:
    duração_parcial_min = 60 - min_ini
    duração_total_min = duração_parcial_min + min_fin
    duração_total_hora = duração_total_hora - 1
elif min_ini < min_fin:
    if hora_ini == hora_fin:
        duração_total_min = min_fin - min_ini
        duração_total_hora = 0
    else:
        duração_total_min = min_fin - min_ini    
elif min_ini == min_fin:
    duração_total_min = 0

print("O JOGO DUROU", duração_total_hora, "HORA(S) E", duração_total_min, "MINUTO(S)")