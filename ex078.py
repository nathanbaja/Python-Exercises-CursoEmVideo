n = list()
for x in range(0,5):
    n.append(int(input('Digite um valor: ')))
n.sort()
print(f'O maior valor digitado foi {n[0]}')
n.sort(reverse=True)
print(f'O menor valor digitado foi {n[0]}')