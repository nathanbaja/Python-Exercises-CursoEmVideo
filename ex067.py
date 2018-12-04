t = 0
while True:
    n = int(input('Digite um numero para calcular a tabuada: '))
    if n < 0:
        break
    print(f'''{n} x{1:3} = {n*1}
{n} x{2:3} = {n*2}
{n} x{3:3} = {n*3}
{n} x{4:3} = {n*4}
{n} x{5:3} = {n*5}
{n} x{6:3} = {n*6}
{n} x{7:3} = {n*7}
{n} x{8:3} = {n*8}
{n} x{9:3} = {n*9}
{n} x{10:3} = {n*10}''')