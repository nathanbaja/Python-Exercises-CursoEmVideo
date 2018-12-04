x = 0
c = 0
while True:
    n = float(input('Digite um numero, [999] para parar: '))
    if n == 999:
        break
    c += n
    x += 1
print(f'{x} numeros foram digitados')
print(f'A soma de todos eles e igual a: {c}')