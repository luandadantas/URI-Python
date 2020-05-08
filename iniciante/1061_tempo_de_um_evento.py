dia_inicio = int(input().split()[1])
hor1, min1, seg1 = input().split(':')
dia_termino = int(input().split()[1])
hor2, min2, seg2 = input().split(':')

hor1 = int(hor1)
hor2 = int(hor2)
min1 = int(min1)
min2 = int(min2)
seg1 = int(seg1)
seg2 = int(seg2)

qtd_dias = dia_termino - dia_inicio
duracao_total_seg = seg2 - seg1
duracao_total_min = min2 - min1
duracao_total_hora = hor2 - hor1

if duracao_total_seg < 0:
    duracao_total_seg += 60
    duracao_total_min -= 1
if duracao_total_min < 0:
    duracao_total_min += 60
    duracao_total_hora -= 1
if duracao_total_hora < 0:
    duracao_total_hora += 24
    qtd_dias -= 1

print(qtd_dias,"dia(s)")
print(duracao_total_hora,"hora(s)")
print(duracao_total_min,"minuto(s)")
print(duracao_total_seg,"segundo(s)")