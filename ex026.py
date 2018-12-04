frase = str(input('digite uma frase ')).strip()
print('existem {} letras "a" nesta frase'.format(frase.lower().count('a')))
print('a primeira letra "a" aparece na posicao {}'.format(frase.lower().find('a')+1))
print('a ultima letra "a" aparece na posicao {}'.format(frase.lower().rfind('a')+1))