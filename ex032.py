ano = int(input('digite um ano qualquer: '))
if ano % 4 == 0:
    print('{} e um ano bissexto'.format(ano))
else:
    print('{} nao e um ano bissexto'.format(ano))