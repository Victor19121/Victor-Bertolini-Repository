num = int(input('Choose a number to see his multiples: '))

for i in range(1, 101, 1):
    print('{} * {:3} = {}'.format(num, i, num*i))



