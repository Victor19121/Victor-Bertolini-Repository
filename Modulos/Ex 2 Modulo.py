import math
from math import sqrt

cateto_1 = int(input('Comprimento do primeiro Cateto: '))
cateto_2 = int(input('Comprimento do segundo Cateto: '))
hipotenusa = math.hypot(cateto_1, cateto_2)
print('A hipotenusa é {}'.format(hipotenusa))
