import math

n = float(input('digite um angulo qualquer '))
s = math.sin(math.radians(n))
c = math.cos(math.radians(n))
tg = math.tan(math.radians(n))

print('O seno deste angulo é igual a {:.2f}\nSeu coseno é igual a {:.2f}\nSua tangente é igual a {:.2f}'
      .format(s, c, tg))
