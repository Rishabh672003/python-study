a = 0
try:
    for a in []:
        try:
            b = float(input('Enter a number: '))
            a = a + b
            print(a)
        except:
            print('bad idea')

except:
    print('bad idea')
