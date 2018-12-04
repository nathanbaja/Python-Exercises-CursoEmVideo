a = int(input('Digite um numero para se calcular o fatorial: '))
b = a
res = 1
while a > 1:
    res *= a
    a -= 1
print('{}! e igual a {}'.format(b, res))