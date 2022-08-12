a = open('mbox-short')
b = a.read()
# print(b)
for word in a:
    word = word.rstrip()
    if word.find('From') == -1:
        continue
    print(word)

# fhand = open('mbox-short')
# for line in fhand:
#     line = line.rstrip()
#     if line.find('@uct.ac.za') == -1:
#         continue
#     print(line)
