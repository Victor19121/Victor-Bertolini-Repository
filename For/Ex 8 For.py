# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo desconsiderando os espaços

ask = str(input("Let's verify if the word is palindrome: "))
no_space = ask.replace(" ", "")
no_space_inverted = no_space[::-1]
inverted = no_space[::-1]
if no_space == no_space_inverted:
    print("It's palindrome!")
else:
    print("It's not palindrome!")



