# a = open('romeo')
# b = a.read()
# c = []
# delimiter = ''
# d = b.split()
# # print(d)
# for words in d:
#     if words not in c:
#         c.append(words)
#         c.sort()
# print(c)
# a = open('mbox-short')
# b = a.read()
# for line in a:
#     lines = line.split()
#     if len(lines) == 0:
#         print('hi')
#         continue
#     if lines[0] != 'From':
#         continue
#     print(lines[0])

a = open('mbox-short')
for line in a:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    words = line.split()
    print(words[1])
