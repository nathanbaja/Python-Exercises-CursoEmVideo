s = 0
t = 0
for x in range(1, 501):
    if x % 2 != 0:
        if x % 3 == 0:
            s = s + 1
            t += x
print('{} valores foram solicitados'.format(s))
print('a soma destes valores da {}'.format(t))
