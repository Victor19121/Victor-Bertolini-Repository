# Faça um programa que leia um ano qualquer e mostre se ele é bissexto
for num in range(1, 2023):
#    num = int(input('Diga um ano: '))
    if num % 100 != 0:
        if num % 4 == 0:
            print('{} É bissexto'.format(num))

    if num % 100 == 0:
        if num % 400 == 0:
            print('{} É bissexto'.format(num))


