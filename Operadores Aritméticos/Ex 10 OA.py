# Escreva um programa que converta uma temperatura
# digitada em celcius para F

c = float(input('Qual a temperatura? '))
f = (c * 9 / 5) + 32
print('A temperatura {}°C é {}°F'.format(c, f))
