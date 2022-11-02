import random

a = str(input('Digite o nome do primeiro: '))
b = str(input('Digite o nome do segundo: '))
c = str(input('Digite o nome do terceiro: '))
d = str(input('Digite o nome do quarto: '))

lista = [a, b, c, d]
random.shuffle(lista)
print(lista)