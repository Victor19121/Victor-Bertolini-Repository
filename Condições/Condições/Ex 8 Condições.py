# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
# se elas podem ou não formam um triângulo

a = int(input('Digite o primeiro lado: '))
b = int(input('Digite o segundo lado: '))
c = int(input('Digite o terceiro lado: '))
print('~' * 30)
maior = a

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

if maior < ((a+b+c)-maior):
    print('Esse triângulo pode existir!')
else:
    print('Esse triângulo não pode existir!')