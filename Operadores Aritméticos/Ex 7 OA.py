# Faça um programa que leia a largura e a altura
# em uma parede em metros, calcule sua área e a
# quantidade de tinta necessária para pintá-la
# sabendo que cada litro de tinta pinta uma área de 2m²

height = float(input('What is the height? '))
width = float(input('What is the width? '))
area = height * width
liters = area / 2
print("The area of the wall is {} and you will need {} liters of ink".format(area, liters))
