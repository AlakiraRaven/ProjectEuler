a = 1
b = 2
s = b


Fib = [a, b]


for i in range(1, 10):
    c = a+b
    Fib.append(c)
    a = b
    b = c

print(Fib)

a = 1
b = 2
c = 0

while c < 4e6:
    c = a+b
    a = b
    b = c
    print('c =' + str (c))

    if c % 2 == 0:
        s += c

print(s)

