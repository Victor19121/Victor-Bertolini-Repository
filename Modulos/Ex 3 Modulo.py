import math
angulo = int(input('Qual o angulo? '))
angulo = math.radians(angulo)
# Seno
seno = math.sin(angulo)
print('O seno do angulo é {:.2f}'.format(seno))
# Cosseno
cosseno = math.cos(angulo)
print('O cosseno do angulo é {:.2f}'.format(cosseno))
# Tangente
tan = math.tan(angulo)
print('A tangente do angulo é {:.2f}'.format(tan))
