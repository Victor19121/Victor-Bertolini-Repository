# Crie um programa que leia o ano de nascimento de 7 pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas são maiores


adult = 0
not_adult = 0
for ask in range(0, 7):
    ask = int(input('What year were you born? '))
    if ask < 2004:
        adult += 1
    else:
        not_adult += 1

print('Here we have {} adults and {} not adults.'.format(adult, not_adult))
