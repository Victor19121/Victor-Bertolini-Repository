# Crie um programa que simule um caixa eletrônico. No início pergunte ao usuário qual valor
# será sacado. E o programa vai informar quantas cedulas de cada valor serão entregues.
# Considere que o caixa eletroncio possui cédulas de 50, 20, 10 e 1

num = int(input("Quanto você quer sacar? R$ "))

res_50 = num % 50
nota_50 = (num - res_50) / 50

res_20 = res_50 % 20
nota_20 = (res_50 - res_20) / 20

res_10 = res_20 % 10
nota_10 = (res_20 - res_10) / 10

nota_01 = res_10

a = f"Você receberá {nota_50} nota(s) de R$50.00"
b = f"Você receberá {nota_20} nota(s) de R$20.00"
c = f"Você receberá {nota_10} nota(s) de R$10.00"
d = f"Você receberá {nota_01} nota(s) de R$1.00"

if nota_50 != 0:
    print(a)
if nota_20 != 0:
    print(b)
if nota_10 != 0:
    print(c)
if nota_01 != 0:
    print(d)


