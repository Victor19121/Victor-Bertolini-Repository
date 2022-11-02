# Escreva um programa que leia dois números inteiros e compare-os,
# mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# Não existe valor maior, os dois são iguais

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
maior = a

if b > a:
    print('O segundo número é maior com: {}'.format(b))
elif a > b:
    print('O primeiro número é maior com: {}'.format(a))
else:
    print('Os valores {} e {} são iguais!'.format(a, b))

