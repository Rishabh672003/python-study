a = []
total = 0
while True:
    b = input('enter the number: ')
    if b == 'done':
        exit()
    b = int(b)
    a.append(b)
    # for num in range(0, len(a)):
    #     total = total + a[num]
    # print(total)
    print(sum(a))
