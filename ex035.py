# if a < c + b and b < a + c and c < a + b:
#     print('os comprimentos acima PODEM formar um triangulo')
# else:
#     print('os comprimentos acima NAO PODEM formar um triangulo')


print('ANALISADOR DE TRIANGULOS')
a = float(input('comprimento da primera reta '))
b = float(input('comprimento da segunda reta '))
c = float(input('comprimento da terceira reta '))

maior = a

if b > a and b > c:
    maior = b
    if maior <= a + c and maior >= c - a and maior >= a - c:
        print('os comprimentos acima PODEM formar um triangulo')
    else:
        print('os comprimentos acima NAO podem formar um triangulo')
elif c > a and c > b:
    maior = c
    if maior <= a + b and maior >= b - a and maior >= a - b:
        print('os comprimentos acima PODEM formar um triangulo')
    else:
        print('os comprimentos acima NAO podem formar um triangulo')
elif a > b and a > c:
    maior = a
    if maior <= b + c and maior >= c - b and maior >= b - c:
        print('os comprimentos acima PODEM formar um triangulo')
    else:
        print('os comprimentos acima NAO podem formar um triangulo')

elif maior == a == c or maior <= a + c and maior >= c - a and maior >= a - c:
    print('os comprimentos acima PODEM formar um triangulo')
else:
    print('os comprimentos acima NAO podem formar um triangulo')