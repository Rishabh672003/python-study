import string

a = open('romeo')
b = dict()
for line in a:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    words = line.split()
    for word in words:
        if word not in b:
            b[word] = 1
        else:
            b[word] += 1

print(b)
string.punctuation
