# eng2sp = dict()
# # print(eng2sp)
# # eng2sp['one'] = 'uno'
# # print(eng2sp)
# eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
# print(eng2sp)
# print(eng2sp['two'])

a = open('words')
b = a.read()
c = b.rsplit()
d = dict()
for word in c:
    d[word] = 'lol'
print(d)
print('the' in d)
