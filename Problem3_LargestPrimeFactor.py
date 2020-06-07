'''
the code works for smaller numbers, does not scale well
'''

import math

if __name__ == "__main__":
    x = 0

    x = int(input('Please input a positive integer X: '))

    while x < 0:
        print('Your number is negative, please input a positive value.')
        x = int(input('Please input a positive integer X: '))

    print('Nice \n')

    BiggestValue = 0

    for i in range(2, int((math.sqrt(x))+1)):
        if x % i == 0:
            BiggestValue = i
            x = x/i


    print('The largest prime factor is: ', end='')
    print(BiggestValue)