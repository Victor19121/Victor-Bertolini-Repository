soma = 0
for i in range(1, 7):
    num = int(input('Digite o {}° número: '.format(i)))

    discover = num % 2
    if discover == 0:
        soma = soma + num
    else:
        soma += 0

print('A soma dos números é = {}'.format(soma))
print('System finished!')
