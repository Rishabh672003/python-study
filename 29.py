# a = 'done-my exam'
# b = a.split('-')
# print(b)

# a = ['a', 'b']
# delimiter = ' '
# c = delimiter.join(a)
# print(c)

a = open('mbox.txt')
for line in a:
    line = line.rstrip()
    if not line.startswith('Return-Path'): continue
    words = line.split()
    print(words[1])
