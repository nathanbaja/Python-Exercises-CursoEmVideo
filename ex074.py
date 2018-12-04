# print(f'O menor numero gerado foi: {min(numeros)}')
# print(f'O maior numero gerado foi: {max(numeros)}')

import random
numeros = (random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10))
x = sorted(numeros)
print(f'Os numeros gerados foram: {numeros}')
print(f'O menor numero gerado foi: {x[0]}')
print(f'O maior numero gerado foi: {x[-1]}')