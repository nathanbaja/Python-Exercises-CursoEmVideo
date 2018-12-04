from datetime import date

ano = date.today().year
a = int(input('Em que ano você nasceu? '))

idade = ano - a
if idade < 9:
    print('Sua categoria é MIRIM')
elif idade >= 9 and idade < 14:
    print('Sua categoria é INFANTIL')
elif idade >= 14 and idade < 19:
    print('Sua categoria é JUNIOR')
elif idade >= 19 and idade < 25:
    print('Sua categoria e SÊNIOR')
else:
    print('Sua categoria é MASTER')