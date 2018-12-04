s = float(input('Qual o seu salario? '))
if (s > 1250):
    s = s + s*10/100
    print('seu novo salario, com aumento de 10% e de {:.2f} reais'.format(s))
else:
    s = s + s*15/100
    print('seu novo salario, com aumento de 15% e de {:.2f} reais'.format(s))