hora_inicial, hora_final = input().split()

hora_inicial = int(hora_inicial)
hora_final = int(hora_final)

if hora_inicial > hora_final:
    duracao_parcial = 24 - hora_inicial
    duracao_total = duracao_parcial + hora_final 
elif hora_final > hora_inicial:
    duracao_total = hora_final - hora_inicial
elif hora_inicial == hora_final:
    duracao_total = 24    
    
print("O JOGO DUROU", duracao_total, "HORA(S)")    