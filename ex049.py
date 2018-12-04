print('='*11)
print('{: ^11}'.format('TABUADA'))
print('='*11)
x = int(input('Deseja ver a tabuada de qual numero? '))
a = 0
for n in range(0, 10):
    a += 1
    s = x * a
    print('{} x {: ^3} = {: ^3}'.format(x, a, s))