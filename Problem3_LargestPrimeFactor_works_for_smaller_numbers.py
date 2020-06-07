'''
the code works for smaller numbers, does not scale well
'''

import math

def IfPrime (x):
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range (3, int (math.sqrt(x)+1), 2):
        if x % i == 0:
            return False
    return True

if __name__ == "__main__":
           
    x = 0

    x = int(input('Please input a positive integer X: '))

    while x < 0:
        print('Your number is negative, please input a positive value.')
        x = int(input('Please input a positive integer X: '))

    print('Nice \n')

    # print('Now, let me check the prime factors of your number and list them below')

    # for i in range(1, int (math.sqrt(x)+1)):
    #     if x % i == 0:
    #         print (i)
    # values =[]
    BiggestValue = 0

    for i in range(2, int ((x/2)+1)):
        if x % i == 0:
            p = IfPrime(i)
            # print(f'i: {i}, is_prime: {p}')
            if p is True and i > BiggestValue:
                # print (i)
                # values.append(i)
                BiggestValue = i
                # print(i)


    print('The largest prime factor is: ', end = '')
    print(BiggestValue)


    # print(values[-1])

    # r = 0

    # for i in values:
    #     if  i > r:
    #         r = i

    # print(r)