print('-'*40)
print(f'{"LISTAGEM DE PRECOS":^40}')
print('-'*40)

lista = ('Asus PRIME B350M-K', 409.90, '1x8gb DDR4', 398.00, 'Ryzen 1600', 730.00, 'Corsair CX550', 266.90, 'GTX 1070', 1500.00)
print(f'''{lista[0]:.<30}R$ {lista[1]:>7.2f}
{lista[2]:.<30}R$ {lista[3]:>7.2f}
{lista[4]:.<30}R$ {lista[5]:>7.2f}
{lista[6]:.<30}R$ {lista[7]:>7.2f}
{lista[8]:.<30}R$ {lista[9]:>7.2f}''')
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}',end='')
    else:
        print(f'R$ {lista[pos]:>7.2f}')
print('-'*40)