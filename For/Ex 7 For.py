# Faça um programa que leia um número inteiro e diga se ele é ou não primo


num = int(input('Say a number: '))
mult = 0

for count in range(2, num):
    if num % count == 0:
        print('É multiplo de: {}'.format(count))
        mult = mult + 1
if mult == 0:
    print('É primo')
else:
    print('Tem {} multiplos acima de 2 e abaixo de {}'.format(mult, num))

