N = int(input())
list_sequence = [0,1]

while len(list_sequence) != N:
    next_number = list_sequence[-2] + list_sequence[-1]
    list_sequence.append(next_number)

print(*list_sequence)
