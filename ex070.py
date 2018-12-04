menor = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
total = 0
maior = 0
nome = ''
while True:
    n = str(input('Nome do produto comprado: ')).strip().upper()
    p = float(input('Preco do produto comprado: '))
    esc = str(input('Deseja continuar: [S/N] ')).strip().upper()
    total += p
    if esc != 'N' and esc != 'NAO' and esc != 'S' and esc != 'SIM':
        print('Comando invalido, tente novamente')
        break
    if p > 1000:
        maior += 1
    if p < menor:
        menor = p
        nome = n
    elif p == 0:
        menor = p
    if esc == 'N' or esc == 'NAO':
        break
print(f'O total destes produtos foi de {total:.2f} reais')
print(f'O produto mais barato foi: {nome}. Que custou {menor:.2f} reais')
print(f'{maior} produtos foram mais caros do que 1000 reais')