from random import randint

contador = 0
soma = 0
ask = 0
key = randint(1, 1000)
while ask != key:
    ask = int(input('Try to guess the number: '))
    soma = soma + ask
    contador += 1
    if ask > key:
        print('Too High!')
    elif ask < key:
        print('Too Low')
total = soma - key
print("You found the key, the sum of your numbers is {} in {} tries.".format(total, contador))