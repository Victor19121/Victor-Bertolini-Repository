initial = int(input('Digit any number to start the AP: '))
ratio = int(input('Digit any number to create a ratio: '))

for i in range(1, 10):
    initial = initial + ratio
    print(' {} '.format(initial), end='→')
