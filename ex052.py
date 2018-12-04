import math

n = (float(input('Digite um numero: ')))
if n == 2 or n == 3 or n == 5 or n == 7:
    print('{} e um numero primo'.format(n))
elif n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0:
    print('{} e um numero primo'.format(n))
else:
    print('{} nao e um numero primo'.format(n))
