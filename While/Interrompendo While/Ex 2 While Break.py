# Faça um programa que mostre a tabuada de vários números, um de cada vez para cada valor digitado
# O programa será interrompido quando o número solicitado for negativo

while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    if num < 0:
        break
    for i in range(1, 11):
        result = num * i
        print(f'{num} x {i:2} = \033[33m{result}\033[m')
    print('\033[36m=-\033[m'*35)

