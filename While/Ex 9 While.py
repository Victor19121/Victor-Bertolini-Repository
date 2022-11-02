# Crie um programa que leia vários números inteiros pelo teclado
# No final da execução, mostre a média entre todos os valores
# E qual foi o maior e menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

existencia = True
contador = total = 0
ask = 0
continuar = ""
maior = 0
menor = 0
while existencia == True:
    ask = int(input('Say a number: '))
    total = total + ask
    contador += 1
    if contador == 1:
        menor = maior = ask
    else:
        if ask > maior:
            maior = ask
        if ask < menor:
            menor = ask

    permanece = str(input('Do you want to continue?(Y/N) ')).upper().strip()[0]
    if permanece == 'Y':
        existencia = True
    elif permanece == 'N':
        existencia = False
    else:
        print("Sorry, I couldn't understand...")

mean = total / contador
print("The biggest value is {}, the smallest is {}, the mean of the numbers is {}".format(maior, menor, mean))
