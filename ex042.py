# if a < c + b and b < a + c and c < a + b:
#     print('os comprimentos acima PODEM formar um triangulo')
# else:
#     print('os comprimentos acima NAO PODEM formar um triangulo')


print('ANALISADOR DE TRIANGULOS')
a = float(input('comprimento da primera reta '))
b = float(input('comprimento da segunda reta '))
c = float(input('comprimento da terceira reta '))

if a ==  b == c:
    print('Estas medidas PODEM formar um triangulo e elas formam um triangulo EQUILATERO')
elif a != b != c:
    if a > b > c:
        if a > b - c and a < b + c:
            print('Estas medidas PODEM formar um triangulo e elas formam um triangulo ESCALENO')
        else:
            print('Estas medidas NAO PODEM formar um triangulo')
    elif a > c > b:
        if a > c - b and a < c + b:
            print('Estas medidas PODEM formar um triangulo e elas formam um triangulo ESCALENO')
        else:
            print('Estas medidas NAO PODEM formar um triangulo')
    elif b > a > c:
        if b > a - c and b < a + c:
            print('Estas medidas PODEM formar um triangulo e elas formam um triangulo ESCALENO')
        else:
            print('Estas medidas NAO PODEM formar um triangulo')
    elif b > c > a:
        if b > c - a and b < c + a:
            print('Estas medidas PODEM formar um triangulo e elas formam um triangulo ESCALENO')
        else:
            print('Estas medidas NAO PODEM formar um triangulo')
    elif c > a > b:
        if c > a - b and c < a + b:
            print('Estas medidas PODEM formar um triangulo e elas formam um triangulo ESCALENO')
        else:
            print('Estas medidas NAO PODEM formar um triangulo')
    elif c > b > a:
        if c > b - a and c < b + a:
            print('Estas medidas PODEM formar um triangulo e elas formam um triangulo ESCALENO')
        else:
            print('Estas medidas NAO PODEM formar um triangulo')
else:
    if a > (b == c) or a < (b == c):
        if a > b - c and a < b + c:
            print('Estas medidas PODEM formar um triangulo e elas formam um triangulo ISÓSCELES')
        else:
            print('Estas medidas NAO PODEM formar um triangulo')
    elif b > (a == c) or b < (a == c):
        if b > a - c and b < a + c:
            print('Estas medidas PODEM formar um triangulo e elas formam um triangulo ISÓSCELES')
        else:
            print('Estas medidas NAO PODEM formar um triangulo')
    elif c > (a == b) or c < (a == b):
        if c > a - b and c < a + b:
            print('Estas medidas PODEM formar um triangulo e elas formam um triangulo ISÓSCELES')
        else:
            print('Estas medidas NAO PODEM formar um triangulo')

