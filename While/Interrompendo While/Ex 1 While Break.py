# Crie um programa que leia vários números pelo teclado. O programa só vai parar quando o usuário digitar
# o valor de 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a
# soma entre eles

total = 0
digitos = 0
ask = 0
while True:
    ask = int(input('Digite um número: '))
    if ask == 999:
        break
    ask = str(ask)
    digitos = digitos + len(ask)
    ask = int(ask)
    total = total + ask
print(f'A quantidade de digitos foi: {digitos} e a soma entre os números digitados é: {total}')

