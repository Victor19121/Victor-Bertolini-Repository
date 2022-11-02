# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999.
# que é a condição de parada.
# No final mostre quantos números foram digitados e qual foi a soma entre eles

contador = 0
soma = 0
ask = 0
while ask != 999:
    ask = int(input('Try to guess the number: '))
    soma = soma + ask
    contador += 1
    if ask != 999:
        print('Try again')
total = soma - 999
print("You found the key, the sum of your numbers is {} in {} tries.".format(total, contador))
