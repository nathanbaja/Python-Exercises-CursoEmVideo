h = 0
m = 0
p18 = 0
while True:
    i = int(input('Quantos anos voce tem? '))
    s = str(input('Qual seu sexo? ')).strip().lower()
    esc = str(input('Deseja continuar? ')).strip().lower()
    if i >= 18:
        p18 += 1
    if s == 'f' or s == 'feminino':
        if i < 20:
            m += 1
    if s == 'm' or s == 'masculino':
        h += 1
    if s != 'm' or s != 'masculino' or s != 'f' or s != 'feminino':
        print('Sexo invalido, tente novamente')
        break
    if esc != 'sim' and esc != 's' and esc != 'nao' and esc != 'n':
        print('Opcao invalida, tente novamente')
        break
    elif esc == 'n' or esc == 'nao':
        break
print(f'{p18} pessoas tem mais de 18 anos')
print(f'{m} mulheres tem menos de 20 anos')
print(f'{h} homens foram cadastrados')