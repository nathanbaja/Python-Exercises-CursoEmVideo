print('=-'*12)
print('BEM-VINDO AO NOSSO BANCO')
print('=-'*12)
n = 0
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
cont5 = 0
cont6 = 0
p = int(input('Qual valor deseja sacar? '))
while True:
    if n + 100 <= p:
        n += 100
        cont1 += 1
    elif n + 50 <= p:
        n += 50
        cont2 += 1
    elif n + 20 <= p:
        n += 20
        cont3 += 1
    elif n + 10 <= p:
        n += 10
        cont4 += 1
    elif n + 5 <= p:
        n += 5
        cont5 += 1
        if n == p-1 or n+3 == p:
            n -= 5
            n += 2
            cont5 -= 1
            cont6 += 1
    elif n + 2 <= p:
        n += 2
        cont6 += 1
    if n == p:
        break

print(cont1, cont2, cont3, cont4, cont5, cont6)
print(f'Total de {cont1} cedulas de 100 reais')
print(f'Total de {cont2} cedulas de 50 reais')
print(f'Total de {cont3} cedulas de 20 reais')
print(f'Total de {cont4} cedulas de 10 reais')
print(f'Total de {cont5} cedulas de 5 reais')
print(f'Total de {cont6} cedulas de 2 reais')
