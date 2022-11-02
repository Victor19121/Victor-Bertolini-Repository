# Escreva um programa que leia um valor
# em metros e o exiba convertido em centimetros
# e milimetros

ask = float(input("Write the value in meters to convert: "))
cm = ask * 100
ml = ask * 1000

print('{} meters is {} centimeters and {} millimeters.'.format(ask, cm, ml))
