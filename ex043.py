p = float(input('Digite seu peso: '))
a = float(input('Digite sua altura em metros: '))

imc = p / (a*a)

if a > 2.3:
    print('Altura invalida, digite o valor em metros, exemplo: 1.83')
elif imc < 18.5:
    print('Voce esta abaixo do peso ideal')
elif imc >= 18.5 and imc < 25:
    print('Voce estao no peso ideal')
elif imc >= 25 and imc < 30:
    print('Voce esta acima do peso')
elif imc >= 30 and imc < 40:
    print('Voce esta na obesidade')
else:
    print('Voce esta na obesidade morbida')
print('Seu IMC e: {:.2f}'.format(imc))