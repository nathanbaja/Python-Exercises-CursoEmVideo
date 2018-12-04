x = 's'
s = 0
m = 0
maior = 0
menor = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
while x != 'n':
    n = int(input('Digite um numero: '))
    x = str(input('Deseja continuar? [S/N] ')).strip().lower()
    s += n
    m += 1
    if x != 'n' and x != 's':
        print('Comando invalido, tente novamente')
    elif n < menor:
        menor = n
    elif n > maior:
        maior = n
media = s / m
print('A media entre estes {} numeros e igual a {}'.format(m, media))
print('O maior numero e {} e o menor numero e {}'.format(maior, menor))