# faça um prograama que leia três números e mostre qual é o maior e qual é o menor

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
print('~' * 30)
menor = maior = a
# Menor
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

# Maior
if b < a and b < c:
    menor = b
if c < a and c < b:
    maior = c
print('O maior valor é {} e o menor valor é {}'.format(maior, menor))
