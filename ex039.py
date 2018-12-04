from datetime import date

ano = date.today().year
s = str(input('Qual seu sexo? ')).strip()

if s.lower() == 'feminino' or s.lower() == 'f':
    print('Você é do sexo feminino, nao precisa fazer o alistamento obrigatorio')
elif s.lower() == 'masculino' or s.lower() == 'm':
    a = int(input('Em que ano você nasceu? '))
    saldo = ano - a
    if saldo == 18:
        print('Este é o ano do seu alistamento, corre que da tempo')
    if saldo > 18:
        saldo2 = saldo - 18
        print('Seu alistamento foi há {} anos atras, espero que tenha comparecido'.format(saldo2))
    if saldo < 18:
        saldo2 = 18 - saldo
        print('Seu alistamento sera daqui {} anos'.format(saldo2))
else:
    print('Opção invalida, tente novamente')