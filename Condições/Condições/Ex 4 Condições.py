# Desenvolva um programa que pergunte a distancia de uma viagem em km
# Calcule o preço da passagem, cobrando 0,5 por km para viagens de até 200km
# e 0,45 para viagens mais longas

ask = int(input('Qual o tamanho do percurso? '))
if ask <=200:
    total = ask * 0.5
    print("O valor da viagem será de: R$\033[36m{}\033[m".format(total))
else:
    total = ask * 0.45
    print("O valor da viagem será de: R$\033[32m{}\033[m".format(total))
