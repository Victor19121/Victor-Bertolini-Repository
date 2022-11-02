# Faça um programa que leia o peso de 5 pessoas.
# No final diga qual o maior e o menor peso.
max_weight = 0
min_weight = 1000
ask = 0
for i in range(0, 5):
    ask = float(input("What's your weight? "))

    if ask >= max_weight:
        max_weight = ask
    if ask <= min_weight:
        min_weight = ask

print('The max weight in this group is: {}'.format(max_weight))
print('The min weight in this group is: {}'.format(min_weight))
