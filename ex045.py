import random

print('Vamos jogar "pedra, papel e tesoura"?')
n = (['PEDRA', 'PAPEL', 'TESOURA'])
x = str(input('Digite sua escolha ')).strip().upper()
a = random.choice(n)
print('JOGADOR escolheu: {}'.format(x))
print('COMPUTADOR escolheu: {}'.format(a))
if x != 'PAPEL' and x != 'PEDRA' and x != 'TESOURA':
    print('Opcao invalida, tente novamente')
elif a == 'PAPEL':
    if x == 'PEDRA':
        print('{} ganha de {}, voce perdeu'.format(a, x))
    elif x == 'PAPEL':
        print('Deu empate, vamos jogar novamente')
    elif x == 'TESOURA':
        print('{} ganha de {}, parabens, voce ganhou'.format(x, a))
elif a == 'PEDRA':
    if x == 'TESOURA':
        print('{} ganha de {}, voce perdeu'.format(a, x))
    elif x == 'PEDRA':
        print('Deu empate, vamos jogar novamente')
    elif x == 'PAPEL':
        print('{} ganha de {}, parabens, voce ganhou'.format(x, a))
elif a == 'TESOURA':
    if x == 'PAPEL':
        print('{} ganha de {}, voce perdeu'.format(a, x))
    elif x == 'TESOURA':
        print('Deu empate, vamos jogar novamente')
    elif x == 'PEDRA':
        print('{} ganha de {}, parabens, voce ganhou'.format(x, a))