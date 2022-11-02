# Elabore um programa que calcule o valor a ser pago
# Por um produto, preço normal e condição de pagamento
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

preco_normal = float(input('Qual o valor do produto? '))
pagamento = int(input('''
Qual será a forma de pagamento?
[1] À vista dinheiro/cheque (10% de desconto)
[2] À vista no cartão (5% de desconto)
[3] Em até 2x no cartão (sem desconto)
[4] Em 3x ou mais no cartão (20% de juros)
'''))

if pagamento == 1:
    preco = preco_normal * 0.9
    print(f"O valor do produto de acordo com a forma de pagamento é {preco}")
elif pagamento == 2:
    preco = preco_normal * 0.95
    print(f"O valor do produto de acordo com a forma de pagamento é {preco}")
elif pagamento == 3:
    print(f"O valor do produto de acordo com a forma de pagamento é {preco_normal}")
elif pagamento == 4:
    preco = preco_normal * 1.2
    print(f"O valor do produto de acordo com a forma de pagamento é {preco}")
else:
    print("Sorry, I couldn't understand...")
