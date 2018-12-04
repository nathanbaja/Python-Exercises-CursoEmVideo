import random

a = input('Digite o nome do primeiro aluno ')
b = input('Digite o nome do segundo aluno ')
c = input('Digite o nome do terceiro aluno ')
d = input('Digite o nome do quarto aluno ')


r = random.sample([a, b, c, d], k=4)

print('A ordem de apresentação é {}'.format(r))