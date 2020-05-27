N = int(input())

dentro_intervalo = 0
fora_intervalo = 0

for i in range(N):
    num = int(input())
    if 10 <= num <= 20:
        dentro_intervalo += 1
    else:
        fora_intervalo += 1

print("{} in".format(dentro_intervalo))
print("{} out".format(fora_intervalo))