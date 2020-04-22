tempo = int(input())

horas = tempo // 3600
resto_hora = tempo % 3600
minutos = resto_hora // 60
segundos = tempo % 60

print(str(horas) + ":" + str(minutos) + ":" + str(segundos))