# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso
# de 0 a 20. Seu programa deverá ler um número pelo teclado e mostrá-lo por extenso.

tupla = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "novo", "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
ask = int(input('Escolha um valor entre 0 e 20: '))

while 0 > ask < 20:
    ask = int(input('Valor inexistente, por favor digite um valor entre 0 e 20: '))

print(tupla[ask])

