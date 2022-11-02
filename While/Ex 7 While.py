# Escreva um programa que leia um numero n inteiro qualquer e mostre na tela
# os n primeiros numeros na sequencia de Fibonacci

n = int(input('Diga um número qualquer: '))

num1 = 0
num2 = 1
contador = 2
print("{} → {} →".format(num1, num2), end='')
while contador < n:
    num3 = num2 + num1
    print(" {} →".format(num3), end='')
    num1 = num2
    num2 = num3
    contador = contador + 1

print(' FIM')

# 0,1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584