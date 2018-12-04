# cidade = str(input('digite o nome de sua cidade: '))
# print('sua cidade comeca com a palavra santo? {}'.format('santo ' in cidade[:6].lower()))

cidade = str(input('digite o nome de sua cidade: '))
split = cidade.split()
print('sua cidade comeca com a palavra santo? {}'.format(split[0].lower() == 'santo'))

