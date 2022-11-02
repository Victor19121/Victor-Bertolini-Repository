# Melhore o desafio 61, perguntando para o usuário se ele quer ver mais alguns termos
# O programa encerra quando ele digitar 0

start = int(input('Digit any number to start the AP: '))
ratio = int(input('Digit any number to create a ratio: '))

contador = 0
num = 0
ask = 10
while ask != 0:
    num = num + ask
    while contador < num:
        start = start + ratio
        print(' {} '.format(start), end='→')
        contador += 1
    print('PAUSA')
    ask = int(input('How many terms do you want to see? '))

print('Progressão finalizada com {} termos aparentes.'.format(num))



