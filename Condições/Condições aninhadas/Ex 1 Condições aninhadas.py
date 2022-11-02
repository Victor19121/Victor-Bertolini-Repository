# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar
# calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
# ou então o empréstimo será negado

valor = int(input('Qual o valor da casa? '))
salario = int(input('Qual o salário? '))
anos = int(input('Quantos anos para pagar? '))

meses = anos * 12
parcela = valor / meses
referencia_salario = salario * 0.3
if referencia_salario >= parcela:
    print('Empréstimo aprovado! A parcela ficou em {}'.format(parcela))
else:
    print('Empréstimo negado')