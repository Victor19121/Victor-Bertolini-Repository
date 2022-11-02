from random import randint

def again():
    ask = input("Do you want to play again? (Y/N)").upper()
    if ask == "Y":
        game()
    else:
        print('See you later! Made by Victor Bertolini de Sousa')

def game():
    secret = randint(1, 100)
    print('Welcome to my game!')
    print("Try to guess what number I'm thinking (from 1 to 100)")
    guess = tentative = 0

    while guess != secret:
        tentative += 1
        g = input('What is the number? ')
        guess = int(g)
        if guess == secret:
            print('You Win in tentative {}!'.format(tentative))
            again()
        elif guess > secret:
            print('Too high!')
        elif guess < secret:
            print('Too Low!')
        else:
            print('Try again')
            print('==================================')
game()




