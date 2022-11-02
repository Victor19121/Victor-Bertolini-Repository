# Escreva um programa que faça o computador pensar em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
# O programa deverá escrever na tela se o usuário venceu ou perde
from random import randint

key = randint(1, 5)

guess = int(input('Try to guess the number: '))
if key == guess:
    print('\033[0;43mYOU WIN!!!\033[m')
if key != guess:
    print('\033[0;41mYOU LOSE!!!\033[m')
