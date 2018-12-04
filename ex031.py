n = int(input('digite, em Km, a distancia de uma viagem '))
if (n <= 200):
    v = n*0.5
    print('o valor da sua viagem, cobrando 50 centavos por Km, ficou {} reais'.format(v))
else:
    v = n*0.45
    print('o valor da sua viagem, cobrando 45 centavos por Km, ficou {} reais'.format(v))
print('faca uma boa viagem')