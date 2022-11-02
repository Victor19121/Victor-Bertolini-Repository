from random import randint

sorteio = randint(1, 4)
print('O aluno escolhido foi: ')
if sorteio == 1:
    print('Felix')
elif sorteio == 2:
    print('Astolfo')
elif sorteio == 3:
    print('Gabriel')
else:
    print('Venti')
