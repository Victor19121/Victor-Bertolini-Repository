# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
# para salários superiores a 1250, calcule um aumento de 10%
# para os inferiores ou iguais, o aumento é de 15%

salario = int(input('Qual o valor do seu salário? '))

if salario > 1250:
    salario = salario * 1.1
    print('O salário atualizado é: R${}'.format(salario))
else:
    salario = salario * 1.5
    print('O salário atualizado é: R${}'.format(salario))
    
