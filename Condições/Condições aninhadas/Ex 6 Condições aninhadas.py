# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: Infantil
# Até 19 anos: junior
# até 20 anos: senior
# acima: master

idade = int(input('Qual o ano que você nasceu? '))
idade = 2022 - idade

if idade <= 9:
    print('Categoria Mirim')
elif 9 < idade <= 14:
    print('Categoria Infantil')
elif 14 < idade <= 19:
    print('Categoria Júnior')
elif 19 < idade <= 20:
    print('Categoria Sênior')
else:
    print('Categoria Master')
