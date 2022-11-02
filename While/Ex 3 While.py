# Crie um programa que leia 2 valores e mostre um menu na tela
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos numeros
# [5] sair do programa
def programa():
    existencia = 1
    while existencia:
        num1 = int(input('Insira o primeiro valor: '))
        num2 = int(input('Insira o segundo valor: '))

        menu = int(input('''
        Digite o numero da opção selecionada:
        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos numeros
        [5] sair do programa
        '''))

        if menu == 1:
            print(num1 + num2)
            print('A soma de {} e {} é igual a {}'.format(num1, num2, num1 + num2))
            existencia = False

        elif menu == 2:
            print(num1 * num2)
            print('A multiplicação de {} e {} é igual a {}'.format(num1, num2, num1 * num2))
            existencia = False

        elif menu == 3:
            if num1 > num2:
                print('O maior número é {}'.format(num1))
            elif num1 < num2:
                print('O maior número é {}'.format(num2))
            else:
                print('{} e {} são iguais'.format(num1, num2))
            existencia = False

        elif menu == 4:
            existencia = True

        elif menu == 5:
            existencia = False

def again():
    ask = input('Do you want to calculate again?(Y/N) ').upper().strip()[0]
    if ask == 'Y':
        programa()
        again()
    elif ask == 'N':
        print('''
        I swear you liked the calculator!
        Made by: Victor Bertolini de Sousa''')
    else:
        print("I couldn't understand what you said")
        again()

programa()
again()





