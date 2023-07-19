# a = 'done-my exam'
# b = a.split('-')
# print(b)

# a = ['a', 'b']
# delimiter = ' '
# c = delimiter.join(a)
# print(c)

a = open('mbox.txt')
count = 0
for line in a:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    if line.startswith('From'):
        count = count + 1
    words = line.split()
    print(words[1])
print(count)
