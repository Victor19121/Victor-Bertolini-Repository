# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar
# Se é hora de se alistar
# Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

idade = int(input('Em que ano você nasceu? '))

if idade > 2004:
    tempo = 2022 - idade
    tempo = 18 - tempo
    print('Você ainda vai se alistar! Faltam {} anos'.format(tempo))

elif idade < 2004:
    tempo = 2004 - idade
    print('Você já passou do prazo de se alistar em {} anos'.format(tempo))

else:
    print('É hora de se alistar!')
