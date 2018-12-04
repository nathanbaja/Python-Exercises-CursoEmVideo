a = int(input('Digite um numero '))
b = int(input('Digite um numero '))
c = int(input('Digite um numero '))
d = int(input('Digite um numero '))
ns = (a, b, c, d,)
print(f'Voce digitou {ns.count(9)} vezes o numero 9')
if 3 in ns:
    print(f'O primeiro 3 aparece na posicao {ns.index(3)+1}')
x = 0
print(f'Os numeros pares digitados foram: ',end='')
for x in ns:
    if x % 2 == 0:
        print(x,'', end='')