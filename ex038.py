n1 = float(input('Digite um numero qualquer: '))
n2 = float(input('Digite outro numero qualquer: '))

if n1 > n2:
    print('{} e maior que {}'.format(n1, n2))
elif n2 > n1:
    print('{} e maior que {}'.format(n2, n1))
else:
    print('{} e igual a {}'.format(n1, n2))