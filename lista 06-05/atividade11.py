num_3 = 3
num_7 = 7
num_9 = 9
num_25 = 25
num_26 = 26

fatorial_3 = 1
fatorial_7 = 1
fatorial_9 = 1
fatorial_25 = 1
fatorial_26 = 1

for num in range (1, num_3+1):
    fatorial_3 *= num

for num in range (1, num_7+1):
    fatorial_7 *= num

for num in range (1, num_9+1):
    fatorial_9 *= num

for num in range (1, num_25+1):
    fatorial_25 *= num

for num in range (1, num_26+1):
    fatorial_26 *= num

print(f"O fatorial de {num_3} é: {fatorial_3}")
print(f"O fatorial de {num_7} é: {fatorial_7}")
print(f"O fatorial de {num_9} é: {fatorial_9}")
print(f"O fatorial de {num_25} é: {fatorial_25}")
print(f"O fatorial de {num_26} é: {fatorial_26}")