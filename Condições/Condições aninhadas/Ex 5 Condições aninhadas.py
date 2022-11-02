# Crie um programa que leia duas notas de um aluno e calcule a sua média
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5: REPROVADO
# - Média entre 5 e 6.9: RECUPERAÇÃO
# - Média 7 ou superior: APROVADO

nota_1 = float(input('Digite a primeira nota: ').replace(',', '.'))
nota_2 = float(input('Digite a segunda nota: ').replace(',', '.'))
media = (nota_1 + nota_2) / 2

if media >= 7:
    print('O aluno está aprovado com a nota {}'.format(media))
if 5 < media < 7:
    falta = 7 - media
    print('O aluno está de recuperação com a nota {}, faltam {} para ser aprovado'.format(media, falta))
if media <= 5:
    print('O aluno está reprovado com a nota {}'.format(media))


