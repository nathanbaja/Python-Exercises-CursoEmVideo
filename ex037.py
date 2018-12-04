
print('='*18)
print('CONVERSOR NUMERICO')
print('='*18)
n = int(input('Digite um numero inteiro qualquer '))
print('Escolha uma base de conversao')
print('1 para binario')
print('2 para octal')
print('3 para hexadecimal')
escolha = str(input('Sua Opcao: '))

if escolha == '1':
    print('O numero {} convertido para binario e igual a {}'.format(n, bin(n)[2:]))
elif escolha == '2':
    print('O numero {} covertido para octal e igual a {}'.format(n, oct(n)[2:]))
elif escolha == '3':
    print('O numero {} convertido para hexadecimal e igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opcao invalida, digite somente "1", "2" ou "3"')