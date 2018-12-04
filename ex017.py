## from math import sqrt

## o = float(input('digite o comprimeto de um dos catetos do triangulo '))
## a = float(input('digite o comprimento do outro cateto '))

## h1 = o**2
## h2 = a**2
## h3 = h1 + h2
## print('a o comprimento da hipotenusa deste triangulo é de {:.2f} centimetros'.format(sqrt(h3)))

from math import hypot

o = float(input('digite o comprimeto de um dos catetos do triangulo '))
a = float(input('digite o comprimento do outro cateto '))

h = hypot(o, a)

print('a o comprimento da hipotenusa deste triangulo é de {:.2f} centimetros'.format(h))