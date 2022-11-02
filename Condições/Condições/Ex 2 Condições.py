# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite
print('\033[33m=-\033[m'*30)
ask = float(input('Qual a sua velocidade? '))
if ask > 80:
    acima = ask - 80
    total = acima * 7
    print('Você foi multado por \033[7;31mexcesso\033[m de velocidade! Deverá pagar: R${}'.format(total))
elif ask <= 80:
    print('Você está dirigindo dentro das normas desta via!')

