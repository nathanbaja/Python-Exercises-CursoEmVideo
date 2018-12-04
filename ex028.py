import random

n = random.randint(0,10)

n2 = int(input('tente adivinhar o numero de 0 a 10 '))
if (n2 == n):
    print('parabens, voce acertou')
else:
    print('voce errou, o numero era {}'.format(n))

