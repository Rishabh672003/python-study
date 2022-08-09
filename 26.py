# a = input('enter a string: ')
# count1 = 0
# count2 = 0
# for letter in a:
#     if letter.isupper() == True:
#         count1 = count1 + 1
#     else:
#         count2 = count2 + 1
# print(count1)
# print(count2)

# def is_good(x):
#     count1 = 0
#     count2 = 0
#     for y in x:
#         if y.isupper() == True:
#             count1 = count1 + 1
#         else:
#             count2 = count2 + 1
#     return count1, count2
# a = input("enter a string: ")
# print(is_good(a))


def rang(x, y, z):
    x = int(x)
    y = int(y)
    z = int(z)
    if x in range(y, z):
        print(x, 'is in range', '(', y, ',', z, ')')


a = input('first number: ')
b = input('range start: ')
c = input('range finish: ')
rang(a, b, c)
