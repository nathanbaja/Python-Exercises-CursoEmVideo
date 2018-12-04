n1 = float(input('Digite a primeira nota '))
n2 = float(input('Digite a segunda nota '))
n3 = float(input('Digite a terceira nota '))

m = (n1 + n2 + n3) / 3

if m < 5:
    print('Sua media foi {:.2f}, sinto muito, mas você esta REPROVADO'.format(m))
elif m >= 5 and m < 7:
    print('Sua media foi {:.2f}, você esta em RECUPERAÇAO'.format(m))
elif m >= 7 and m <= 10:
    print('Sua media foi {}, parabens, você esta APROVADO'.format(m))