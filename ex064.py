x = 1
c = 0
s = 0
while x != 0:
    n = int(input('Digite um numero, [999] para parar: '))
    c += 1
    s += n
    if n == 999:
        break
print('Voce digitou {} numeros'.format(c - 1))
print('A soma destes numeros e igual a {}'.format(s - 999))