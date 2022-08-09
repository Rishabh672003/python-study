a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0 ]
b = []
for num in a:
    if num % 2 == 0:
        b.append(num)
        b.sort()
print(b)


# b = []
# c = []
# while True:
#     a = input('enter the numbers: ')
#     if a == 'done':
#         break
#     b.append(a)
#     for num in b:
#         if num % 2 == 0:
#             c.append(num)
# print(c)

