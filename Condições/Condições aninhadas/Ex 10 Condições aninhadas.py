# Crie um programa que faça o computador jogar
# jokenpô com você

from random import randint

num = randint(1, 3)

user = int(input('''Escolha a sua jogada.
\033[36m[1] Pedra
[2] Papel
[3] Tesoura\033[m
'''))
# Pedra
if user == 1:
    if num == 1:
        print('=-'*30)
        print('''Jogador jogou PEDRA 
Computador jogou PEDRA''')
        print('=-' * 30)
        print('EMPATE')
    elif num == 2:
        print('=-' * 30)
        print('''Jogador jogou PEDRA  
Computador jogou PAPEL''')
        print('=-' * 30)
        print('PERDEU')
    elif num == 3:
        print('=-' * 30)
        print('''Jogador jogou PEDRA  
Computador jogou TESOURA''')
        print('=-' * 30)
        print('GANHOU')

# Papel
if user == 2:
    if num == 2:
        print('=-' * 30)
        print('''Jogador jogou PAPEL 
Computador jogou PAPEL''')
        print('=-' * 30)
        print('EMPATE')
    elif num == 3:
        print('=-' * 30)
        print('''Jogador jogou PAPEL 
Computador jogou TESOURA''')
        print('=-' * 30)
        print('PERDEU')
    elif num == 1:
        print('=-' * 30)
        print('''Jogador jogou PAPEL 
Computador jogou PEDRA''')
        print('=-' * 30)
        print('GANHOU')

# Tesoura
if user == 3:
    if num == 3:
        print('=-' * 30)
        print('''Jogador jogou TESOURA
Computador jogou TESOURA''')
        print('=-' * 30)
        print('EMPATE')
    elif num == 1:
        print('=-' * 30)
        print('''Jogador jogou TESOURA
Computador jogou PEDRA''')
        print('=-' * 30)
        print('PERDEU')
    elif num == 2:
        print('=-' * 30)
        print('''Jogador jogou TESOURA
Computador jogou PAPEL''')
        print('=-' * 30)
        print('GANHOU')



