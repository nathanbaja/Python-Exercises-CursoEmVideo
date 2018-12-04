from datetime import date
ano = date.today().year
a = 0
b = 0
for x in range(0,7):
    nasc = int(input('Digite o ano em que voce nasceu: '))
    if ano - nasc > 18:
        a += 1
    else:
        b += 1
print('{} pessoas sao maiores de idade'.format(a))
print('{} pessoas sao menores de idade'.format(b))