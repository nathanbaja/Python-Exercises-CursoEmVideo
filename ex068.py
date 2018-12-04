import random

print('='*26)
print('VAMOS JOGAR PAR OU IMPAR?')
print('='*26)
v = 0
while True:
    x = str(input('Voce quer PAR ou IMPAR? ')).strip().upper()
    m = int(input('Digite um numero de 1 a 10: '))
    n = random.randint(1, 10)
    print(f'O COMPUTADOR jogou {n}')
    print(f'O JOGADOR jogou {m}')
    if x == 'PAR' or x == 'P':
        if (n + m) % 2 == 0:
            v += 1
            print(f'{n} + {m} = {n+m}, e {n+m} e PAR, o JOGADOR ganhou')
            print('')
        elif(n + m) % 2 != 0:
            print(f'{n} + {m} = {n+m}, e {n+m} e IMPAR, o COMPUTADOR ganhou')
            print('')
            break
    elif x == 'IMPAR' or x == 'I':
        if (n + m) % 2 == 0:
            print(f'{n} + {m} = {n+m}, e {n+m} e PAR, o COMPUTADOR ganhou')
            print('')
            break
        else:
            v += 1
            print(f'{n} + {m} = {n+m}, e {n+m} e IMPAR, o JOGADOR ganhou')
            print('')
    else:
        print('Comando invalido, tente novamente')
        break
print(f'O jogador ganhou {v} vezes consecutivas')