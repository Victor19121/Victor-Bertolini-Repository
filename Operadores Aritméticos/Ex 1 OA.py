# Faça um programa que leia um número inteiro
# e mostre na tela o seu sucessor e seu antecessor

print('-='*30)
ask = int(input('Choose a number: '))
ant = ask - 1
suc = ask + 1
print("The number chose is {}, it's successor is {} and it's predecessor is {}".format(ask, suc, ant))
