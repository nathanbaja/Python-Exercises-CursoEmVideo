menor = 9999999999999
maior = 0
y = 0
for x in range(0, 5):
    y += 1
    p = float(input('peso da {}ª pessoa: '.format(y)))
    if p > maior:
        maior = p
    else:
        maior = maior
    if p < menor:
        menor = p
    else:
        menor = menor
print('o maior peso e {} e o menor peso e {}'.format(maior, menor))