codigo_DDD = int(input())

codigo_DDD_dict = {
    61: 'Brasilia',
    71: 'Salvador',
    11: 'Sao Paulo',
    21: 'Rio de Janeiro',
    32: 'Juiz de Fora',
    19: 'Campinas',
    27: 'Vitoria',
    31: 'Belo Horizonte'
}

if codigo_DDD in codigo_DDD_dict:
    print(codigo_DDD_dict[codigo_DDD])
else:
    print('DDD nao cadastrado')