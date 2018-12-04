import random
a = 1
x = random.randint(1, 10)
r = int(input('Tente adivinhar o numero que estou pensando: '))
while r != x:
    a += 1
    r = int(input('Infelizmente voce errou, tente de novo: '))
print('Parabens, voce acertou, precisou de {} tentativas'.format(a))