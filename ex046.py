import emoji
from time import sleep

for x in range(10,-1,-1):
    print(x)
    sleep(1)
    if x == 0:
        print('FELIZ ANO NOVO!!!')
        print(emoji.emojize(' :fireworks:'*5, use_aliases=True))