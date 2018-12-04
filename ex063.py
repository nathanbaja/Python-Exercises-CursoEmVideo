n = int(input('Digite um numero: '))
x = 0
a = 0
b = 1
print(a)
print(b)
while x < n:
    c = b + a
    a = b
    b = c
    print(c)
    x += 1