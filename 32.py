# eng2sp = dict()
#
# eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
# # a = eng2sp['one']
# # b = len(eng2sp)
# # print(b)
# # d = list(eng2sp.values())
# # print('uno' in d )
# e = eng2sp.get('go', 1)
# eng2sp['go'] = 'home'
# print(e)

# a = open('words')
# b = a.read()
# c = b.rsplit()
# d = dict()
# for word in c:
#     d[word] = ''
# print(d)
# print('the' in d)

a = 'kurzgezsagtz'
d = {}
for c in a:
    d[c] = d.get(c, 0) + 1
print(d)
e = d.get('z')
print(e)
