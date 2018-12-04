k = int(input('Quantos quilometros este carro percorreu? '))
d = int(input('por quantos dias ele foi alugado? '))

km = k * 0.15
dias = d * 60
res = km + dias

print('esse carro percorreu {} Km em {} dias, o custo de seu aluguel é de {} reais'.format(k, d, res))