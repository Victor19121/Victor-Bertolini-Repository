# Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla
# No final mostre: Quantas vezes apareceu o valor 9, Em que posição foi digitado o primeiro valor 3
# os numeros pares

num_1 = int(input('Digite um número: '))
num_2 = int(input('Digite um número: '))
num_3 = int(input('Digite um número: '))
num_4 = int(input('Digite um número: '))

tupla = (num_1, num_2, num_3, num_4)
lista = []
for i in tupla:
    print(i, end='-->')
    lista.append(i)
print(lista)
posições = [int(a) for a in lista]
print(posições)