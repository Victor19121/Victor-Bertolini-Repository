# Faça um programa que leia um numero qualquer e mostre o seu fatorial

ask = int(input('Digite um numero e veja o seu fatorial: '))
count = 1
result = 1
while count <= ask:
    result = result * count
    count = count + 1
  #  print(result)
 #   print('***************************** {} *****************************'.format(count))


print(result)