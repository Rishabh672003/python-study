import operator
a = {'a':'1' ,'b':'2', 'c': '3'}
b = a.values()
print(b)
c = list(b)
# print(c)
print(c[::-1])
sorted_d = sorted(a.items(), key= operator.itemgetter(1), reverse=True)
print(sorted_d)
