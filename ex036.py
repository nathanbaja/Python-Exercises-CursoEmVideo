print('='*20)
print('EMPRESTIMO BANCARIO')
print('='*20)
casa = int(input('Qual o valor da casa que deseja comprar? '))
salario = float(input('Qual o valor do seu salario? '))
anos = int(input('Em quantos anos deseja pagar esta casa? '))
mensal = casa/(anos*12)
if mensal > (salario*0.3):
    print('Para comprar uma casa de {:.2f} reais, voce pagaria uma mensalidade de {:.2f} reais, isso excede 30% de seu salario'.format(casa, mensal))
    print('Emprestimo NEGADO')
else:
        print('Parabens, emprestimo CONCEDIDO')

    print('Voce pagara uma parcela de {:.2f} reais por mes durante {} anos'.format(mensal, anos))