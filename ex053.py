# inverso = ''
# for reverso in range(len(junto) -1, -1, -1):
#     inverso += junto[reverso]

frase = str(input('Digite uma frase: ')).strip().upper().split()
junto = ''.join(frase)
inverso = junto[::-1]
if inverso == junto:
    print('{} ao contrario fica {}'.format(junto, inverso))
    print('Isto e um palindromo')
else:
    print('{} ao contrario fica {}'.format(junto, inverso))
    print('Isto nao e um palindromo')