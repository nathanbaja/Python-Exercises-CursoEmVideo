v = int(input('digite a velocidade do carro '))
if (v > 80):
    m = (v - 80)
    multa = m*7
    print('voce foi multado, o valor da multa e de {} reais'.format(multa))
else:
    print('voce nao foi multado, parabens')