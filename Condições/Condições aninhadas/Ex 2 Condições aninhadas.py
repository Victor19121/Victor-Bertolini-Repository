# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
# a base de conversão 1 para binário, 2 para octal, e 3 para hexadecimal

num = int(input('Digite um número: '))
ask = int(input('''
Para qual base você quer converter esse número?
[1] Binário
[2] Octal
[3] Hexadecimal
'''))

if ask == 1:
    num = bin(num)
    print(num[2::])
elif ask == 2:
    num = oct(num)
    print(num[2::])
elif ask == 3:
    num = hex(num)
    print(num[2::])
else:
    print('Desculpe eu não entendi!')
