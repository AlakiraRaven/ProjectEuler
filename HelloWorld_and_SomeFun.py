x = 'Hello World'

s = 'Sander'
m = 'Marta'

ListOfNames = [m, s]
l = []

print(x + ', ' + s + ' and ' + m)


for i in range(len(ListOfNames)):
    print(x + ', ' + ListOfNames[i])


for name in ListOfNames:
    print(x + ', ' + name)


for i in range(2, 20):
    if i % 2 == 0:
        print(i)
    else:
        print('Eh' + i*'eh' + ', ' 'STUPID')
