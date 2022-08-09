# numlist = list()
# while True:
#     inp = input('enter a number: ')
#     if inp == 'done':
#         break
#     value = float(inp)
#     numlist.append(value)
# average = sum(numlist) / len(numlist)
# print(numlist)
# print(average)
# print(set(numlist))
# if len(numlist) > len(set(numlist)):
#     print(numlist)
#     pass
#
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5])) 
