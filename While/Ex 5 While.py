# Refaça o desafio 51, lendo o primeiro termo e a razão da PA.
# Mostrando os 10 primeiros termos utilizando a estrutura while

start = int(input('Digit any number to start the AP: '))
ratio = int(input('Digit any number to create a ratio: '))

contador = 0
while contador < 10:
    start = start + ratio
    print(' {} '.format(start), end='→')
    contador += 1
