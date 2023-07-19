# largest = None
# print('Before:', largest)
# for itervar in [3, 41, 12, 9, 74, 15]:
#     if largest is None or itervar > largest:
#         largest = itervar
#     print('Loop:', itervar, largest)
# print('Largest:', largest)

#
# def min1(values):
#     smallest = None
#     for value in values:
#         if smallest is None or value < smallest:
#             smallest = value
#     return smallest
#
#
# a = [1, 2, 4, 6, 6, 0]
# min1(1)
#
# smallest = None
# print('Before:', smallest)
# for itervar in [3, 41, 12, 9, 74, 15]:
#     if smallest is None or itervar < smallest:
#         smallest = itervar
#     print('Loop:', itervar, smallest)
# print('Smallest:', smallest)
a = min(3, 41, 12, 9, 74, 15)
print(a)
