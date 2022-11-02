# Crie um programa que leia quanto dinheiro uma pessoa tem
# na carteira e mostre quantos dólares ela pode comprar

ask = float(input('How many R$ do you have? '))
dolar = ask/3.27
print('You can buy US${} dollars'.format(dolar))
