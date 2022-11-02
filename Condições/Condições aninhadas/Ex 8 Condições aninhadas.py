# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: abaixo do peso
# entre 18.5 e 25 Peso ideal
# 25 até 30 Sobrepeso
# 30 até 40 obesidade
# acima de 40: Obesidade mórbida

massa = float(input('Digite a sua massa: '))
altura = float(input('Digite sua altura em metros: '))

# Cálculo do IMC
imc = massa / (altura * altura)

print(f'Seu IMC é {imc}')
