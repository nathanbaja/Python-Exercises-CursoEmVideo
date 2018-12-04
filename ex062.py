a = float(input('Digite o primeiro termo de uma PA: '))
b = float(input('Digite sua razao: '))
x = 0
m = 10
n = 0
while x < m and m > 0:
    print(a)
    a+=b
    x+=1
    if x == m:
        m = int(input('Quer ver mais termos? Quantos? '))
        x = 0
        while n < m:
            n+=1
            if m == 0:
                break
