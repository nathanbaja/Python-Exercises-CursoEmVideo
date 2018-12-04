p = 0
age = 0
maior = 0
menor20 = 0
homem = ''
for x in range(0, 4):
    p += 1
    n = str(input('Nome da {}ª pessoa: '.format(p))).strip().upper()
    i = float(input('Idade da {}ª pessoa: '.format(p)))
    s = str(input('Sexo da {}ª pessoa: '.format(p))).strip().upper()
    age += i
    if s != 'F' and s != 'M' and s != 'FEMININO' and s != 'MASCULINO':
        print('Sexo invalido, tente novamente')
        break
    elif s == 'M' or s == 'MASCULINO':
        if i > maior:
            maior = i
            homem = n
        else:
            maior = maior
    elif s == 'F' or s == 'FEMININO':
        if i < 20:
            menor20 += 1
        else:
            menor20 = menor20
media = age / p
print('A media de idade das pessoas do grupo e {}'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maior, homem))
print('{} das mulheres sao menores de 20 anos'.format(menor20))