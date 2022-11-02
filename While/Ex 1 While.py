# Faça um programa que leia o sexo de uma pessoa, mas aceite valores M ou F.
# Caso esteja errado peça a digitação correta até obter um valor correto

sexo = str(input('Qual o seu sexo? [M/F] ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos, insira novamente o seu sexo: ')).upper().strip()[0]
print('Dados válidos!')
