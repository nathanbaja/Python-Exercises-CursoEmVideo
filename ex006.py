print('Receba um numero e mostre dobro, triplo e raiz')

n = float(input('digite um numero '))

d = n*2
t = n*3
r = n**(1/2)

print('seu dobro é {}, seu triplo é {} e sua raiz é {:.3f}'.format(d, t, r))