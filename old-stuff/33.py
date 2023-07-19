fname = open('romeo')

counts = dict()
for word in fname:
    words = word.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(len(counts))
print(counts.keys())
for key in counts:
    if counts[key] > 1:
        print(key, counts[key])

