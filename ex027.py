nome = str(input('digite seu nome completo: ')).strip()
split = nome.split()
print('Seu primeiro nome e: {}'.format(split[0]))
split.reverse()
print('Seu ultimo nome e: {}'.format(split[0]))