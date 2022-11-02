# Escreva um programa que pergunte a quantidade de km
# percorridos por um carro alugado e a quantidade de
# dias pelos quasi ele foi alugado. Calcule o preço
# a pagar sabendo que o carro custa R$60 por dia
# e R$0,15 por km rodado.

dias = int(input('Quantos dias o carro foi alugado? '))
rodado = int(input('Quantos quilometros foram percorridos? '))
preco = (60*dias) + (0.15*rodado)

print('O preço do aluguel foi de: {}'.format(preco))
