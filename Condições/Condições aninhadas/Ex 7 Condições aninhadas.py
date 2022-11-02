# Refaça o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triângulo será formado
# equilátero, isósceles, escaleno

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
    if a == b == c:
        print('Ele é equilátero')
    elif a != b != c:
        print('Ele é escaleno')
    else:
        print('Ele é isósceles')
else:
    print('Esse triângulo não pode existir!')