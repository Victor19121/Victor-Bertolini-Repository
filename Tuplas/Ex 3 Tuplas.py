# Crie um programa que sorteie 5 números aleatórios e coloque em uma Tupla
# depois disso mostre a listagem dos números e também indique o maior e menor número da tupla
from random import randint
maior = menor = 0
contador = 0
a = randint(1, 10)
b = randint(1, 10)
c = randint(1, 10)
d = randint(1, 10)

tupla = (a, b, c, d)
print(f'Os números sorteados são: {tupla}')
for num in tupla:
    contador += 1
    # Maior
    if maior < num:
        maior = num
    # Menor
    if contador == 1:
        menor = num
    else:
        if num < menor:
            menor = num
print(f'O maior valor é {maior} e o menor é {menor}')



