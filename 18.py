import math
# def x(y):
#     while y > 1:
#         a = y*(y - 1)
#         y -=1
#         return a
#
# a = int(input("enter a number: "))
# print(x(a))


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# n = int(input('Input a number to compute the factiorial : '))
# print(factorial(n))

def x(y):
    a  = math.factorial(y)
    return a
print(x(10))
