n1 = float(input('digite o primeiro numero '))
n2 = float(input('digite o segundo numero '))
n3 = float(input('digite o terceiro numero '))

if (n1 > n2) and (n1 > n3):
    print('{} e o maior numero'.format(n1))
if (n2 > n1) and (n2 > n3):
    print('{} e o maior numero'.format(n2))
if (n3 > n1) and (n3 > n2):
    print('{} e o maior numero'.format(n3))
if (n1 < n2) and (n1 < n3):
    print('{} e o menor numero'.format(n1))
if (n2 < n1) and (n2 < n3):
    print('{} e o menor numero'.format(n2))
if (n3 < n1) and (n3 < n2):
    print('{} e o menor numero'.format(n3))
else:
    print('algum numero esta repetido, tente novamente')

