import random

a = input('digite o nome do primeiro aluno ')
b = input('digite o nome do segundo aluno ')
c = input('digite o nome do terceiro aluno ')
d = input('digite o nome do quarto aluno ')

r = random.choice([a, b, c, d])
print('O aluno sorteado foi: {}'.format(r))