s = str(input('Digite seu sexo:[M/F] ')).strip().lower()
while s != 'm' and s != 'f':
    print('Opcao invalida, tente novamente')
    s = str(input('Digite seu sexo:[M/F] ')).strip().lower()
print('parabens')