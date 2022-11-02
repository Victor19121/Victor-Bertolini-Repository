# Crie um programa que leia um numero inteiro e mostre na tela se ele é par ou ímpar
def definir():
    num = int(input('Diga um número: '))
    if num % 2 == 0:
        print('É \033[0;36mPAR\033[m!')
    elif num % 2 == 1:
        print('É \033[0;35mIMPAR\033[m!')


def again():
    ask = input('Do you want to continue?(Y/N) ').upper().strip()[0]
    if ask == "Y":
        definir()
        again()
    elif ask == "N":
        print('See you later!')
    else:
        print("Sorry, I couldn't understand you...")
        again()


definir()
again()
