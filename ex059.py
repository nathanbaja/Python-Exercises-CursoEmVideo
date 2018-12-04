a = float(input('Digite um numero: '))
b = float(input('Digite mais um numero: '))
escolha = 0
while escolha != 5:
    escolha = int(input('''O que deseja fazer com estes numeros?
    1 para somar
    2 para multiplicar
    3 para saber qual e o maior
    4 para digitar novos numeros
    5 para sair '''))
    if escolha == 1:
        print('{} + {} e igual a {}'.format(a, b, a+b))
    elif escolha == 2:
        print('{} x {} e igual a {}'.format(a, b, a*b))
    elif escolha == 3:
        if a > b:
            print('{} e maior do que {}'.format(a,b))
        elif b > a:
            print('{} e maior do que {}'.format(b,a))
        else:
            print('Estes numeros sao iguais')
    elif escolha == 4:
        a = float(input('Escolha um novo numero: '))
        b = float(input('Escolha outro novo numero: '))
    elif escolha == 5:
        break
    else:
        print('Opcao invalida, tente novamente')
