# fruit = 'banana'
# print(fruit[0:1])
# print(len(fruit))

# stri = 'rishabh'
# for c in stri:
#     reversi = stri[::-1]
# print(reversi)


def string_reverse(x):
    rstr1 = ''
    index = len(x)
    while index > 0:
        rstr1 += x[index - 1]
        index = index - 1
    return rstr1

y = input("enter a string: ")
print(string_reverse(y))
# print(string_reverse('1234abcd'))
