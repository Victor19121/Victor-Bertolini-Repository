# Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador
# Perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

from random import randint
victories = 0
while True:
    contador = 0
    finger = randint(0, 10)
    quest = str(input("Odds or Evens?(O/E) ")).upper().strip()[0]
    ask = int(input('Prepare your fingers: '))

    if ask < 0 or ask > 10:
        print("I think you don't have this amount of fingers...")

    soma = finger + ask
    # If Odd
    if soma % 2 == 0:
        if quest == 'O':
            contador = 1
        else:
            contador = 0
    # If Even
    if soma % 2 == 1:
        if quest == 'E':
            contador = 1
        else:
            contador = 0
    # Result
    print(
        f"The computer chose \033[1;95m{finger}\033[m, you chose Even and \033[1;95m{ask}\033[m, the sum is"
        f" \033[1;95m{soma}\033[m so")
    if contador == 1:
        print("\033[1;33mYOU WIN!!!\033[m")
        victories = victories + 1
        print("\033[1;95m=-\033[m" * 35)
    elif contador == 0:
        print("\033[31mYOU LOSE!!!\033[m")
        print(f"Your number of victories is: {victories}")
        break
    # Again loop



