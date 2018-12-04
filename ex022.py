# nome = input('Digite seu nome completo ')
# split = nome.split()

# print('seu nome em letras maiusculas e: {}'.format(nome.upper()))
# print('seu nome em letras minuscilas e: {}'.format(nome.lower()))
# print('seu primeiro nome e {} e contem {} letras'.format(split[0], len(split[0])))
# print('seu nome contem {} letras ao total'.format(len(''.join(split))))

nome = str(input('digite seu nome completo: ')).strip()
split = nome.split()

print('seu nome em letras maiusculas e {}'.format(nome.upper()))
print('seu nome em letras minuscilas e: {}'.format(nome.lower()))
print('seu primeiro nome e {} e contem {} letras'.format(split[0], nome.find(' ')))
print('seu nome contem {} letras ao total'.format(len(nome) - nome.count(' ')))
